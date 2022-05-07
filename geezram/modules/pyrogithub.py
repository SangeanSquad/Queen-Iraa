import aiohttp
import sys
import heroku3
from pyrogram import filters
from pyrogram.types import Message
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from geezram import pbot, BOT_USERNAME, UPSTREAM_REPO, U_BRANCH, OWNER_ID, DEV_USERS, HEROKU_API_KEY, HEROKU_APP_NAME
from geezram.utils.errors import capture_err
from os import environ, execle


__mod_name__ = "Github"


def fetch_heroku_git_url(api_key, app_name):
    if not api_key:
        return None
    if not app_name:
        return None
    heroku = heroku3.from_key(api_key)
    try:
        heroku_applications = heroku.apps()
    except:
        return None
    heroku_app = None
    for app in heroku_applications:
        if app.name == app_name:
            heroku_app = app
            break
    if not heroku_app:
        return None
    return heroku_app.git_url.replace("https://", "https://api:" + api_key + "@")

@pbot.on_message(filters.command(["github", "git", f"git@{BOT_USERNAME}"]))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)


REPO_ = UPSTREAM_REPO
BRANCH_ = U_BRANCH
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

@pbot.on_message(filters.command("grupdate") & filters.user(OWNER_ID))
async def updatebot(_, message: Message):
    msg = await message.reply_text("**updating bot, please wait for a while...**")
    try:
        repo = Repo()
    except GitCommandError:
        return await msg.edit("**invalid git command !**")
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "upstream" in repo.remotes:
            origin = repo.remote("upstream")
        else:
            origin = repo.create_remote("upstream", REPO_)
        origin.fetch()
        repo.create_head(U_BRANCH, origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    if repo.active_branch.name != U_BRANCH:
        return await msg.edit(
            f"**sorry, you are using costum branch named:** `{repo.active_branch.name}`!\n\nchange to `{U_BRANCH}` branch to continue update!"
        )
    try:
        repo.create_remote("upstream", REPO_)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(U_BRANCH)
    if not HEROKU_URL:
        try:
            ups_rem.pull(U_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await run_cmd("pip3 install --no-cache-dir -r requirements.txt")
        await msg.edit("**update finished, restarting now...**")
        args = [sys.executable, "python3 -m geezram"]
        execle(sys.executable, *args, environ)
        sys.exit()
        return
    else:
        await msg.edit("`heroku detected!`")
        await msg.edit(
            "`updating and restarting is started, please wait for 5-10 minutes!`"
        )
        ups_rem.fetch(U_BRANCH)
        repo.git.reset("--hard", "FETCH_HEAD")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(HEROKU_URL)
        else:
            remote = repo.create_remote("heroku", HEROKU_URL)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except BaseException as error:
            await msg.edit(f"🚫 **updater error** \n\nTraceBack : `{error}`")
            return repo.__del__()
