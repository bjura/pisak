"""
Module to govern all the user's directories that are used by Pisak applications.
"""
import os

from gi.repository import GLib

from pisak import res, logger


_LOG = logger.get_logger(__name__)


# ---------------------------

# HOME general specification

# ---------------------------

"""
Path to the user's home directory.
"""
HOME = os.path.expanduser("~")

"""
Path to a folder in user's home directory. Contains any files that user has
added and wants them to be available inside of some of the Pisak applications
or files that user has access to and can modify them in order to achieve some
kind of different behaviour or look of some of the Pisak applications.
"""
HOME_PISAK_DIR = os.path.join(HOME, ".pisak")


# ------------------------------

# HOME files and subdirectories

# ------------------------------
"""
Path to the configurations directory.
"""
HOME_PISAK_CONFIGS = os.path.join(HOME_PISAK_DIR, "configs")


"""
Path to the favouritess directory.
"""
HOME_PISAK_FAVOURITES = os.path.join(HOME_PISAK_DIR, "favourites")


"""
Path to the databases directory.
"""
HOME_PISAK_DATABASES = os.path.join(HOME_PISAK_DIR, "databases")


"""
Path to the main configuration file avalaible for the user.
"""
HOME_MAIN_CONFIG = os.path.join(HOME_PISAK_CONFIGS, "main_config.ini")

"""
Directory with logging files.
"""
HOME_LOGS_DIR = os.path.join(HOME_PISAK_DIR, "logs")

"""
Directory that contains custom icons created by the user. Each icon's name has
to correspond to the name of an generic icon that it is supposed to replace.
Accepted format of an icon file is SVG.
"""
HOME_ICONS_DIR = os.path.join(HOME_PISAK_DIR, "icons")

"""
Path to a subdirectory in user's home Pisak directory. Contains files in
json format, created and added by user when one wants to change the graphical
layout of some of the Pisak applications. Files structure: main 'json' folder
contains subfolders, each for every application, named as the related
application name, then each of these subfolders contains one or more json
files, each file with the same name as of the related view and 'json' extension.
"""
HOME_JSON_DIR = os.path.join(HOME_PISAK_DIR, "json")

"""
Path to a subdirectory in user's home Pisak directory. Contains files in
css format, created and added by user when one wants to change the look of
some elements of a graphical interface or of the whole view of some of
the Pisak applications. Files structure: in this folder there can be one
css file for every application, name of each file must be the same as the
application name with 'css' extension.
"""
HOME_STYLE_DIR = os.path.join(HOME_PISAK_DIR, "css")

"""
Path to the css file that styles the blog post for
"blog" application.
"""
HOME_BLOG_STYLE = os.path.join(HOME_STYLE_DIR, "blog_style.css")

"""
Folder in user's home Pisak directory, that contains custom made symbols
to be used within the 'symboler' application.
Each custom made symbol replaces a default one or, if there is no default,
extends the collection of all symbols.
"""
HOME_SYMBOLS_DIR = os.path.join(HOME_PISAK_DIR, "symbols")


"""
Folder in user's home Pisak directory, that contains custom sounds which can be played
during scanning and button selection.
"""
HOME_SOUNDS_DIR = os.path.join(HOME_PISAK_DIR, "sounds")


"""
Path to the spreadsheet containing custom symbols topology for
"symboler" application.
"""
HOME_SYMBOLS_SHEETS = os.path.join(HOME_PISAK_DIR, "symboler_sheets")

"""
Path to the symbols model for "symboler" application.
"""
HOME_SYMBOLS_MODEL = os.path.join(HOME_PISAK_DIR, "symbols_model.ini")

"""
Path to the symbols entries file generated by "symboler" application.
"""
HOME_SYMBOLS_ENTRY = os.path.join(HOME_PISAK_DIR, "symbols_entry.ini")

"""
Path to a file containing all information and list of URLs to blogs that are being
followed by the user.
"""
HOME_FOLLOWED_BLOGS = os.path.join(HOME_PISAK_DIR, "followed_blogs.ini")

"""
Path to a file with all the blog settings or configuration parameters, like: user
credentials, blog address etc.
"""
HOME_BLOG_CONFIG = os.path.join(HOME_PISAK_CONFIGS, "blog_config.ini")

"""
Path to a file where all the necessary setting of an email account are stored.
"""
HOME_EMAIL_CONFIG = os.path.join(HOME_PISAK_CONFIGS, "email_config.ini")

"""
Path to the file with email application address book.
"""
HOME_EMAIL_ADDRESS_BOOK = os.path.join(
    HOME_PISAK_DATABASES, "email_address_book.db")

"""
Database with info about text files generated by the 'speller' application.
"""
HOME_TEXT_DOCUMENTS_DB = os.path.join(HOME_PISAK_DATABASES,'documents.db')


# ---------------------------

# Default system directories

# ---------------------------

"""
Dictionary with paths to various file system default directories.
"""
USER_FOLDERS = {
    "desktop": GLib.USER_DIRECTORY_DESKTOP,
    "documents": GLib.USER_DIRECTORY_DOCUMENTS,
    "downloads": GLib.USER_DIRECTORY_DOWNLOAD,
    "music": GLib.USER_DIRECTORY_MUSIC,
    "pictures": GLib.USER_DIRECTORY_PICTURES,
    "public": GLib.USER_DIRECTORY_PUBLIC_SHARE,
    "templates": GLib.USER_DIRECTORY_TEMPLATES,
    "videos": GLib.USER_DIRECTORY_VIDEOS
}


# ----------------------------------------------------

# Functions managing content from various directories

# ----------------------------------------------------

def get_general_configs():
    """
    Get paths to files with general configuration.

    :returns: list of configuration files, from the most default
    to the most custom one
    """
    configs = []
    default = res.get(os.path.join('configs', 'default_config.ini'))
    if os.path.isfile(default):
        configs.append(default)
    else:
        raise FileNotFoundError(
            "Default general config not found in the res directory.")
    if os.path.isfile(HOME_MAIN_CONFIG):
        configs.append(HOME_MAIN_CONFIG)
    return configs


def get_icon_path(name):
    """
    Get path to an icon with the given name. First look for a custom one in
    user home directory, if nothing found, then look for a default one in
    res directory. Accepted file format is SVG.

    :param name: name of the icon, that is a name of the file containing the
    icon without an extension. Accepted file format is SVG.

    :returns: path to the icon or None if nothing was found
    """
    icon_path = os.path.join(HOME_ICONS_DIR, name) + ".svg"
    if not os.path.isfile(icon_path):
        icon_path = os.path.join(res.get('icons'), name) + ".svg"
        if not os.path.isfile(icon_path):
            msg = "Default icon for '{}' not found in the res directory."
            raise FileNotFoundError(msg.format(name))
    return icon_path


def get_css_path(skin='default'):
    """
    Get css file with the global style description for the whole program.
    Hierarchy of directories being scanned in search for the proper file is
    as follows: first the pisak directory in user's home,
    then css folder in res.

    Structure of style related directories: in pisak folder in user's home -
    'css' folder with css files named the same as the given skin;
    in res directory - the same as in the home.

    :param skin: name of the skin or None for default css

    :returns: path to css file
    """
    css_path = os.path.join(HOME_STYLE_DIR, skin) + ".css"
    if not os.path.isfile(css_path):
        style_dir = res.get("css")
        css_path = os.path.join(style_dir, skin) + ".css"
        if not os.path.isfile(css_path) and skin is not "default":
            css_path = os.path.join(style_dir, "default") + ".css"
    if not os.path.isfile(css_path):
        msg = "Default css not found in the res directory."
        raise FileNotFoundError(msg)
    return css_path


def get_blog_css_path():
    """
    Get css file to style Blog posts.
    """
    css_path = HOME_BLOG_STYLE
    if not os.path.isfile(css_path):
        css_path = os.path.join(res.get('css'),
                                os.path.split(HOME_BLOG_STYLE)[1])
        if not os.path.isfile(css_path):
            msg = "CSS style file for blog post was not found."
            raise FileNotFoundError(msg)
    return css_path


def get_json_path(view, layout='default', app='',):
    """
    Get a json file responsible for building one of the views of the given
    application. Shape of the view is described by 'layout' parameter.
    Hierarchy of directories being scanned in search for the proper file is
    as follows: first the pisak directory in user's home, then json
    directory in res for the specific layout and finally json directory in
    res for the default layout.

    Structure of json related directories: in pisak folder in user's home -
    'json' folder with subfolders for different applications, each named as
    the corresponding application, then in each of them subfolders for
    specific 'layout' with 'json' extended  files inside;
    in res directory - the same as for the home.

    :param view: name of the view
    :param layout: name of the layout of the view or None for default layout
    :param app: name of the application or None, when None then general
    jsons are looked for.

    :returns: path to the json file
    """
    # check home pisak dir
    view_path = os.path.join(HOME_JSON_DIR, app, layout, view) + ".json"
    # if none has been found look in res directory:
    if not os.path.isfile(view_path):
        json_dir = res.get(os.path.join("json", app, layout))
        view_path = os.path.join(json_dir, view) + ".json"
        if not os.path.isfile(view_path) and layout is not "default":
            default_json_dir = res.get(os.path.join("json", app, "default"))
            view_path = os.path.join(default_json_dir, view) + ".json"
    if not os.path.isfile(view_path):
        msg = "Default json for '{}' view of the '{}' application not " \
            "found in the res directory."
        raise FileNotFoundError(msg.format(view, app))
    return view_path


def get_user_dir(folder):
    """
    Get path to one of the XDG user folders.

    :param folder: folder name as str, lowercase, possible are:
    desktop, documents, downloads, music, pictures, public, templates, videos

    :returns: path to XDG user directory
    """
    return GLib.get_user_special_dir(USER_FOLDERS[folder])


def get_sound_path(name):
    """
    Get path to a sound with the given name. First look for a custom sound in
    user home directory, if nothing found, then look for a default sound in
    res directory. Accepted file format is wav.

    :param name: name of the sound file, that is a name of the file without an extension. 
    Accepted file format is WAV.

    :returns: path to the icon or None if nothing was found.
    """
    name = name.lower().replace(' ', '_').replace('\n', '_')
    sound_path = os.path.join(HOME_SOUNDS_DIR, name)
    if not os.path.isfile(sound_path):
        sound_path = os.path.join(res.get('sounds'), name)
        if not os.path.isfile(sound_path):
            _LOG.warning('No sound file found: {}.'.format(sound_path))
    return sound_path
