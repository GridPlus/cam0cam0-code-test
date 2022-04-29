from client import UpdateClient
from update  import Update 

client = UpdateClient()

#Not to overthink this, but a prereq might have a prereq, so recurse
#Recursive case isn't tested, but if there's a nested PrereqUpdate 
#it should apply the updates in the correct order 
def get_prereq_updates(section, prereqs = []):
    download_url = section.get("downloadURL")
    response = client.download_update(download_url)
    version = section.get("TargetVersion")
    appcode = section.get("AppCode")
    update = Update(appcode, response, version)
    prereqs.append(update)
    
    prereq = section.get("PrereqUpdate")
    if prereq is not None:
        return get_prereq_updates(prereq, prereqs)
    else:
        print("prereq is none")
        return prereqs 

def get_updates(catalog, appcode):
    env_section = catalog.get(appcode, None)

    if env_section is not None:
        prereq_section = env_section.get("PrereqUpdate")

        if prereq_section is not None:
            updates = get_prereq_updates(prereq_section)
            for update in updates:
                update.apply()

        download_url = env_section.get("downloadURL")
        if download_url is not None:
            update_content = client.download_update(download_url)
            version = env_section.get("TargetVersion")
            update = Update(appcode, update_content, version)
            update.apply()          

if __name__ == "__main__":
    catalog = client.get_update_catalog()
    get_updates(catalog, "HSM")
    get_updates(catalog, "GCE")





