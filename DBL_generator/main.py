from PIL import Image 
from IPython.display import display 
import random
import json
import sys

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

Background = [
    "Grey", 
    "Greyish Green", 
    "Greyish Yellow", 
    "Light Purple", 
    "Orange", 
    "Peach", 
    "Purple", 
    "Sky Blue", 
    "Tan"
]
Background_weights = [11.1, 11.1, 11.1, 11.1, 11.1, 11.1, 11.1, 11.1, 11.2]

Skins = [ 
    "Amber", 
    "Black Charcoal Dome Skelly",  
    "Black Glower",   
    "Blackish Brown Dome Skelly",   
    "Brainy Blue",   
    "Brainy Brown",   
    "Brainy Green",   
    "Brainy Red",   
    "Brown Cyborg",   
    "Brown Dome Skeleton",   
    "Brown Glower",   
    "Brown Laser Beaming Cyborg",   
    "Charcoal Cyborg",   
    "Charcoal Dome Skeleton",   
    "Charcoal Laser Beaming Cyborg",   
    "Charcoal",   
    "Green Skelly",   
    "Green",   
    "Pink",  
    "Polar White",  
    "Purple",   
    "Red Cyborg",   
    "Red Laser Beaming Cyborg",   
    "Scarred Brown",   
    "Scarred Grey",
    "Purple Reign",
    "Shaded",
    "Teal"
] 
Skins_weights = [3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5]

ClothingOutfit = [
    "Black Burnt DBL Shirt",
    "Black DBL Shirt",
    "Black Logo Tee",
    "Black Tee Security",
    "Burnt Lab Coat",
    "CEO",
    "Deathrow with White Tee",
    "Deathrow",
    "Investor",
    "Lab Coat with White Tee",
    "Lab Coat",
    "Low Risk with White Tee",
    "Low Risk",
    "Security",
    "Sleeveless Rainbow Smile Tee",
    "Sleeveless Rainbow Tee",
    "Sleeveless Smiley  Tee",
    "Sleeveless Tee",
    "Sleevless Slimy Tee",
    "Stained Tanktop",
    "Straitjacket",
    "Unruly with White Tee",
    "Unruly",
    "White Burnt DBL Shirt",
    "White DBL Shirt",
    "White Logo Tee"
]
ClothingOutfit_weights = [3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 5]

Faces = [
    "Alien Moron",
    "Beamer Buffoon",
    "Black Alien Buffoon",
    "Black Buffoon",
    "Black Bulging Laser Beaming Predator",
    "Black Bulging Predator",
    "Black Diamond Mouth Monster",
    "Black Missing Tooth Monster",
    "Black Monster",
    "Black Sus Eyed Moron",
    "Blazer",
    "Broken Lenses Alien Moron",
    "Broken Lenses Alien",
    "Broken Lenses Beamer",
    "Broken Lenses Blazer",
    "Broken Lenses Dragon Breathe",
    "Broken Lenses Moron",
    "Broken Lenses Nicotine Beamer",
    "Broken Lenses Nicotine User",
    "Buffoon",
    "Bulging Buffoon",
    "Bulging Laser Beaming Buffoon",
    "Bulging Moron",
    "Bulging Predator",
    "Chemical Waste",
    "Clumsy Monster",
    "Cyborg",
    "Double Trouble Beamers",
    "Dragon Breathe",
    "Drooling Bulged Eyed Moron",
    "Flared Moron",
    "Gold Grilled Monster",
    "Mini Me",
    "Monster",
    "Moron",
    "Nicotine User Buffoon",
    "No Eyes",
    "Possessed Black Buffoon",
    "Possessed Broken Lenses",
    "Rainbow Monster",
    "Rich Sophisticated Monster",
    "Scarred Monster",
    "Sleeping Black Dragon",
    "Slimed Out Monster",
    "Sophisticated Blazer",
    "Sophisticated Buffoon",
    "Sophisticated Dragon Breathe",
    "Sophisticated Moron",
    "Sophisticated Nicotine User",
    "Sophisticated Twins",
    "Sus Eyed Blazer",
    "Sus Eyed Buffoon",
    "Sus Eyed Dragon Breathe",
    "Sus Eyed Nicotine User",
    "The Predator",
    "Tired Black Monster",
    "Unfazed Broken Lenses",
    "Bandaged Buffoon",
    "Eyepatched Buffoon",
    "Eyepatched Chemical Waste",
    "Eyepatched Predator",
    "Eyepatched Twins"
] 
Faces_weights = [1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6,1.6, 1.6, 1.6, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7]

Headwear = [
    "3rd Eye",
    "Antennas",
    "Arrow",
    "Beaming 3rd Eye",
    "Beaming Black 3rd Eye",
    "Black 3rd Eye",
    "Broken Horn",
    "Bulging 3rd Eye",
    "Devil Horns",
    "Gold Horn",
    "Head Mirror",
    "Rainbow Horn",
    "Sleeping 3rd Eye",
    "Sleeping Black 3rd Eye",
    "Unicorn Horn",
    "none"
] 
Headwear_weights = [3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 50.5]

Necklace = [
    "Ancient Amulet",
    "Beaming Ancient Amulet",
    "Beaming Gold Amulet",
    "Beaming Rainbow Chain",
    "Collar",
    "Diamond Logo Chain",
    "Gold Amulet",
    "Rainbow Chain",
    "Shackles",
    "Shock Collar",
    "none"
]
Necklace_weights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 50]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file nameYARN START

Background_files = {
    "Grey":"Grey",
    "Greyish Green":"Greyish Green",
    "Greyish Yellow":"Greyish Yellow",
    "Light Purple":"Light Purple",
    "Orange":"Orange",
    "Peach":"Peach",
    "Purple":"Purple",
    "Sky Blue":"Sky Blue",
    "Tan":"Tan"
}

Skins_files = {
    "Amber":"Amber",
    "Black Charcoal Dome Skelly":"Black Charcoal Dome Skelly",
    "Black Glower":"Black Glower",
    "Blackish Brown Dome Skelly":"Blackish Brown Dome Skelly",
    "Brainy Blue":"Brainy Blue",
    "Brainy Brown":"Brainy Brown",
    "Brainy Green":"Brainy Green",
    "Brainy Red":"Brainy Red",
    "Brown Cyborg":"Brown Cyborg",
    "Brown Dome Skeleton":"Brown Dome Skeleton",
    "Brown Glower":"Brown Glower",
    "Brown Laser Beaming Cyborg":"Brown Laser Beaming Cyborg",
    "Charcoal Cyborg":"Charcoal Cyborg",
    "Charcoal Dome Skeleton":"Charcoal Dome Skeleton",
    "Charcoal Laser Beaming Cyborg":"Charcoal Laser Beaming Cyborg",  
    "Charcoal":"Charcoal",
    "Green Skelly":"Green Skelly",
    "Green":"Green",
    "Pink" :"Pink" ,
    "Polar White" :"Polar White" ,
    "Purple":"Purple",
    "Red Cyborg":"Red Cyborg",
    "Red Laser Beaming Cyborg":"Red Laser Beaming Cyborg",
    "Scarred Brown":"Scarred Brown",
    "Scarred Grey":"Scarred Grey",
    "Purple Reign":"Purple Reign",
    "Shaded":"Shaded",
    "Teal":"Teal"
}

ClothingOutfit_files = {
    "Black Burnt DBL Shirt":"Black Burnt DBL Shirt",
    "Black DBL Shirt":"Black DBL Shirt",
    "Black Logo Tee":"Black Logo Tee",
    "Black Tee Security":"Black Tee Security",
    "Burnt Lab Coat":"Burnt Lab Coat",
    "CEO":"CEO",
    "Deathrow with White Tee":"Deathrow with White Tee",
    "Deathrow":"Deathrow",
    "Investor":"Investor",
    "Lab Coat with White Tee":"Lab Coat with White Tee",
    "Lab Coat":"Lab Coat",
    "Low Risk with White Tee":"Low Risk with White Tee",
    "Low Risk":"Low Risk",
    "Security":"Security",
    "Sleeveless Rainbow Smile Tee":"Sleeveless Rainbow Smile Tee",
    "Sleeveless Rainbow Tee":"Sleeveless Rainbow Tee",
    "Sleeveless Smiley  Tee":"Sleeveless Smiley  Tee",
    "Sleeveless Tee":"Sleeveless Tee",
    "Sleevless Slimy Tee":"Sleevless Slimy Tee",
    "Stained Tanktop":"Stained Tanktop",
    "Straitjacket":"Straitjacket",
    "Unruly with White Tee":"Unruly with White Tee",
    "Unruly":"Unruly",
    "White Burnt DBL Shirt":"White Burnt DBL Shirt",
    "White DBL Shirt":"White DBL Shirt",
    "White Logo Tee":"White Logo Tee"
}

Faces_files = {
    "Alien Moron": "Alien Moron",
    "Beamer Buffoon": "Beamer Buffoon",
    "Black Alien Buffoon": "Black Alien Buffoon",
    "Black Buffoon": "Black Buffoon",
    "Black Bulging Laser Beaming Predator": "Black Bulging Laser Beaming Predator",
    "Black Bulging Predator": "Black Bulging Predator",
    "Black Diamond Mouth Monster": "Black Diamond Mouth Monster",
    "Black Missing Tooth Monster": "Black Missing Tooth Monster",
    "Black Monster": "Black Monster",
    "Black Sus Eyed Moron": "Black Sus Eyed Moron",
    "Blazer": "Blazer",
    "Broken Lenses Alien Moron": "Broken Lenses Alien Moron",
    "Broken Lenses Alien": "Broken Lenses Alien",
    "Broken Lenses Beamer": "Broken Lenses Beamer",
    "Broken Lenses Blazer": "Broken Lenses Blazer",
    "Broken Lenses Dragon Breathe": "Broken Lenses Dragon Breathe",
    "Broken Lenses Moron": "Broken Lenses Moron",
    "Broken Lenses Nicotine Beamer": "Broken Lenses Nicotine Beamer",
    "Broken Lenses Nicotine User": "Broken Lenses Nicotine User",
    "Buffoon": "Buffoon",
    "Bulging Buffoon": "Bulging Buffoon",
    "Bulging Laser Beaming Buffoon": "Bulging Laser Beaming Buffoon",
    "Bulging Moron": "Bulging Moron",
    "Bulging Predator": "Bulging Predator",
    "Chemical Waste": "Chemical Waste",
    "Clumsy Monster": "Clumsy Monster",
    "Cyborg": "Cyborg",
    "Double Trouble Beamers": "Double Trouble Beamers",
    "Dragon Breathe":"Dragon Breathe",
    "Drooling Bulged Eyed Moron": "Drooling Bulged Eyed Moron",
    "Flared Moron":"Flared Moron",
    "Gold Grilled Monster":"Gold Grilled Monster" ,
    "Mini Me":"Mini Me",
    "Monster":"Monster",
    "Moron":"Moron",
    "Nicotine User Buffoon":"Nicotine User Buffoon",
    "No Eyes":"No Eyes",
    "Possessed Black Buffoon":"Possessed Black Buffoon",
    "Possessed Broken Lenses":"Possessed Broken Lenses",
    "Rainbow Monster":"Rainbow Monster",
    "Rich Sophisticated Monster":"Rich Sophisticated Monster",
    "Scarred Monster":"Scarred Monster",
    "Sleeping Black Dragon":"Sleeping Black Dragon",
    "Slimed Out Monster":"Slimed Out Monster",
    "Sophisticated Blazer":"Sophisticated Blazer",
    "Sophisticated Buffoon":"Sophisticated Buffoon",
    "Sophisticated Dragon Breathe":"Sophisticated Dragon Breathe",
    "Sophisticated Moron":"Sophisticated Moron",
    "Sophisticated Nicotine User":"Sophisticated Nicotine User",
    "Sophisticated Twins":"Sophisticated Twins",
    "Sus Eyed Blazer":"Sus Eyed Blazer",
    "Sus Eyed Buffoon":"Sus Eyed Buffoon",
    "Sus Eyed Dragon Breathe":"Sus Eyed Dragon Breathe",
    "Sus Eyed Nicotine User":"Sus Eyed Nicotine User",
    "The Predator":"The Predator",
    "Tired Black Monster":"Tired Black Monster",
    "Unfazed Broken Lenses":"Unfazed Broken Lenses",
    "Bandaged Buffoon":"Bandaged Buffoon",
    "Eyepatched Buffoon":"Eyepatched Buffoon",
    "Eyepatched Chemical Waste":"Eyepatched Chemical Waste",
    "Eyepatched Predator":"Eyepatched Predator",
    "Eyepatched Twins":"Eyepatched Twins"
}

Headwear_files = {
    "3rd Eye":"3rd Eye",
    "Antennas":"Antennas",
    "Arrow":"Arrow",
    "Beaming 3rd Eye":"Beaming 3rd Eye",
    "Beaming Black 3rd Eye":"Beaming Black 3rd Eye",
    "Black 3rd Eye":"Black 3rd Eye",
    "Broken Horn":"Broken Horn",
    "Bulging 3rd Eye":"Bulging 3rd Eye",
    "Devil Horns":"Devil Horns",
    "Gold Horn":"Gold Horn",
    "Head Mirror":"Head Mirror",
    "Rainbow Horn":"Rainbow Horn",
    "Sleeping 3rd Eye":"Sleeping 3rd Eye",
    "Sleeping Black 3rd Eye":"Sleeping Black 3rd Eye",
    "Unicorn Horn":"Unicorn Horn",
    "none" : "none"
}

Necklace_files = {
    "Ancient Amulet":"Ancient Amulet",
    "Beaming Ancient Amulet":"Beaming Ancient Amulet",
    "Beaming Gold Amulet":"Beaming Gold Amulet",
    "Beaming Rainbow Chain":"Beaming Rainbow Chain",
    "Collar":"Collar",
    "Diamond Logo Chain":"Diamond Logo Chain",
    "Gold Amulet":"Gold Amulet",
    "Rainbow Chain":"Rainbow Chain",
    "Shackles":"Shackles",
    "Shock Collar":"Shock Collar",
    "none": "none"
}

## Generate Traits
TOTAL_IMAGES = 200 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():

    sys.setrecursionlimit(3000)

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(Background, Background_weights)[0]
    new_image ["Skins"] = random.choices(Skins, Skins_weights)[0]
    new_image ["ClothingOutfit"] = random.choices(ClothingOutfit, ClothingOutfit_weights)[0]
    new_image ["Faces"] = random.choices(Faces, Faces_weights)[0]
    new_image ["Headwear"] = random.choices(Headwear, Headwear_weights)[0]
    new_image ["Necklace"] = random.choices(Necklace, Necklace_weights)[0]

    if 'Antennas' in Headwear_files[new_image['Headwear']] or 'Devil Horns' in Headwear_files[new_image['Headwear']]:
        if 'Black Charcoal Dome Skelly' in Skins_files[new_image['Skins']] or 'Blackish Brown Dome Skelly' in Skins_files[new_image['Skins']] or 'Brainy Blue' in Skins_files[new_image['Skins']] or 'Brainy Brown' in Skins_files[new_image['Skins']] or 'Brainy Green' in Skins_files[new_image['Skins']] or 'Brainy Red' in Skins_files[new_image['Skins']] or 'Brown Dome Skeleton' in Skins_files[new_image['Skins']] or 'Charcoal Dome Skeleton' in Skins_files[new_image['Skins']] or 'Green Skelly' in Skins_files[new_image['Skins']]:
            return create_new_image()

    if 'Bandaged Buffoon' in Faces_files[new_image['Faces']] or 'Eyepatched Buffoon' in Faces_files[new_image['Faces']] or 'Eyepatched Chemical Waste' in Faces_files[new_image['Faces']] or 'Eyepatched Predator' in Faces_files[new_image['Faces']] or 'Eyepatched Twins' in Faces_files[new_image['Faces']]:
        if 'Black Charcoal Dome Skelly' in Skins_files[new_image['Skins']] or 'Blackish Brown Dome Skelly' in Skins_files[new_image['Skins']] or 'Brainy Blue' in Skins_files[new_image['Skins']] or 'Brainy Brown' in Skins_files[new_image['Skins']] or 'Brainy Green' in Skins_files[new_image['Skins']] or 'Brainy Red' in Skins_files[new_image['Skins']] or 'Brown Dome Skeleton' in Skins_files[new_image['Skins']] or 'Charcoal Dome Skeleton' in Skins_files[new_image['Skins']] or 'Green Skelly' in Skins_files[new_image['Skins']]:
            return create_new_image()

    if 'Bandaged Buffoon' in Faces_files[new_image['Faces']] or 'Eyepatched Buffoon' in Faces_files[new_image['Faces']] or 'Eyepatched Chemical Waste' in Faces_files[new_image['Faces']] or 'Eyepatched Predator' in Faces_files[new_image['Faces']] or 'Eyepatched Twins' in Faces_files[new_image['Faces']]:
        new_image['Headwear'] = "none"

    if  new_image in all_images:
        return create_new_image()
    else:
        return new_image

# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
  
    new_trait_image = create_new_image()

    all_images.append(new_trait_image)
	
# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

#### Generate Images    
j = 0
for item in all_images:
    
    im1 = Image.open(f'./image/1Background/{Background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./image/2Skins/{Skins_files[item["Skins"]]}.png').convert('RGBA')
    im3 = Image.open(f'./image/3ClothingOutfit/{ClothingOutfit_files[item["ClothingOutfit"]]}.png').convert('RGBA')
    im4 = Image.open(f'./image/4Faces/{Faces_files[item["Faces"]]}.png').convert('RGBA')
    im5 = Image.open(f'./image/5Headwear/{Headwear_files[item["Headwear"]]}.png').convert('RGBA')
    im6 = Image.open(f'./image/6Necklaces/{Necklace_files[item["Necklace"]]}.png').convert('RGBA')

    #Create each composite

    # if not ('Brown Laser Beaming Cyborg' in item["Skins"] or 'Charcoal Laser Beaming Cyborg' in item["Skins"] or 'Red Laser Beaming Cyborg' in item["Skins"] or 'Bandaged Buffoon' in item["Faces"] or 'Eyepatched Buffoon' in item["Faces"] or 'Eyepatched Chemical Waste' in item["Faces"] or 'Eyepatched Predator' in item["Faces"] or 'Eyepatched Twins' in item["Faces"]):
    #     com1 = Image.alpha_composite(im1, im2)
    #     com2 = Image.alpha_composite(im3, im4)
    #     com3 = Image.alpha_composite(im5, im6)
    #     com12 = Image.alpha_composite(com1, com2)
    #     com = Image.alpha_composite(com12, com3)

    # elif 'Brown Laser Beaming Cyborg' in item["Skins"] or 'Charcoal Laser Beaming Cyborg' in item["Skins"] or 'Red Laser Beaming Cyborg' in item["Skins"]:
    #     com1 = Image.alpha_composite(im1, im2)
    #     com2 = Image.alpha_composite(im4, im5)
    #     com12 = Image.alpha_composite(com1, com2)
    #     com = Image.alpha_composite(com12, im6)

    # else:
    #     com1 = Image.alpha_composite(im1, im2)
    #     com2 = Image.alpha_composite(im3, im4)
    #     com12 = Image.alpha_composite(com1, com2)
    #     com = Image.alpha_composite(com12, im6)



    if 'Brown Laser Beaming Cyborg' in item["Skins"] or 'Charcoal Laser Beaming Cyborg' in item["Skins"] or 'Red Laser Beaming Cyborg' in item["Skins"]:
        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(im4, im5)
        com12 = Image.alpha_composite(com1, com2)     
        com = Image.alpha_composite(com12, im6)

    # if 'Bandaged Buffoon' in item["Faces"] or 'Eyepatched Buffoon' in item["Faces"] or 'Eyepatched Chemical Waste' in item["Faces"] or 'Eyepatched Predator' in item["Faces"] or 'Eyepatched Twins' in item["Faces"]:
    #     com1 = Image.alpha_composite(im1, im2)
    #     com2 = Image.alpha_composite(im3, im4)
    #     com12 = Image.alpha_composite(com1, com2)     
    #     com = Image.alpha_composite(com12, im6)
        
    else:
        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(im3, im4)
        com3 = Image.alpha_composite(im5, im6)
        com12 = Image.alpha_composite(com1, com2)
        com = Image.alpha_composite(com12, com3)

    j = j + 1
    #Convert to RGB
    rgb_im = com.convert('RGBA')  

    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
	
#### Generate Metadata for each Image    
f = open('./metadata/all-traits.json',) 
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ape"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "tokenId": token_id,
        "image": str(token_id) + '.png',
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Skins", i["Skins"]))
    token["attributes"].append(getAttribute("ClothingOutfit", i["ClothingOutfit"]))
    token["attributes"].append(getAttribute("Faces", i["Faces"]))
    token["attributes"].append(getAttribute("Headwear", i["Headwear"]))
    token["attributes"].append(getAttribute("Necklace", i["Necklace"]))

    with open('./metadata/' + str(token_id) + '.json', 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()