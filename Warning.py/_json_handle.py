import json
import os
import discord
import sys


class class_warnings:
    def __init__(self):
        pass

    async def object_determin_path_structure(self):
        print('making path if not exsists')
        object_path = os.getcwd()+"/warnings"
        object_path = os.path.exists(object_path)
        if object_path == False:
            object_path = os.getcwd() + "/warnings"
            os.mkdir(object_path)

    async def function_create_user(self, _user):
        object_preset_path = os.getcwd() + "/warnings/"
        object_name = object_preset_path+_user+".json"
        if os.path.isfile(object_name) == True:
            pass
        else:

            object_indent = 4
            object_open_dict = {}
            object_open_dict['ID'] = _user
            object_open_dict['total_warn'] = 0
            object_user = json.dumps(object_open_dict, indent= object_indent)
            object_user = json.loads(object_user)
            with open(object_name, 'w+') as object_json_connected:
                json.dump(object_user, object_json_connected, indent=object_indent)
            object_json_connected.close()

    async def function_reason_guild(self, user_warn, guild_warn, reason_warn):
        object_preset_path = os.getcwd() + "/warnings/"
        object_name = object_preset_path + user_warn + ".json"
        print(object_name)
        var_true_false = True
        with open(object_name, "r") as f:
            object_read_json = json.load(f)
            object_read_json  = json.dumps(object_read_json)
            object_json = json.loads(object_read_json)
            print(object_json)
            f.close()
            try:
                object_json[guild_warn]
                var_true_false = True
            except KeyError:
                var_true_false = False
        print(var_true_false)
        #if the subdirctory does exsists
        if var_true_false == True:
            object_json["total_warn"] += 1
            object_interior = object_json[guild_warn]
            object_interior["warn"] += 1
            var_warn = object_interior["warn"]
            object_interior[var_warn] = reason_warn
            final_object = object_json
        #else
        elif var_true_false == False:
            object_json["total_warn"] += 1
            object_guild_dict = {}
            object_guild_dict["warn"] = 1
            object_guild_dict[1] = reason_warn
            object_json[guild_warn] = object_guild_dict
            final_object = object_json

        with open(object_name,"w+") as f:
            json.dump(final_object, f, indent=4)
            f.close()

    async def discord_embed_warn(self, _Staff,_user, _reason):
        _embed = discord.Embed(title="Warning", description=" ",colour=0xFF0000)
        _em = _embed.add_field
        _rtaff = _Staff.name +"("+str(_Staff.id)+")"
        _embed.set_footer(text=_rtaff)
        _em(name="User details", value="Name of user:\n    {}\n\nID of User:\n     {}".format(_user, _user.id))
        _em(name="Reason", value='||'+_reason+'||')
        return _embed

    async def _get_all_warnings(self, _user_warn_):
        object_preset_path = os.getcwd() + "/warnings/"
        object_name = object_preset_path + _user_warn_ + ".json"
        object_json = "Has a clean record"
        if os.path.isfile(object_name) == True:
            with open(object_name, "r") as f:
                object_json = json.load(f)
                object_json = json.dumps(object_json, indent=4)
        else:
            pass
        return object_json
