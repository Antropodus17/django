# Satisfactory

## Description 
The objective of this project, based on the videogame [satisfactory](https://www.satisfactorygame.com/),is to provide an easy calculator of the cuantity of resources needed to craft other resources.
Once calculated all the resources needed, you could mark them to save the quantity in a session.
Also give a, for the moment, very simple calculator of the energy provide from the generators of the game.

## Dessgin


### 1. Models
In this project we would use two principal models, the generators and the resources:  
- **Generator**:
   - ***ID*** <small style="color:gray">The identifier</small>
   - **Name** <small style="color:gray">Its the name of the generator</small>
   - Power <small style="color:gray">The cuantity of power generated in 100% efficiency</small>
- **Resource**: 
   - ***ID*** <small style="color:gray">The identifier</small>
   - **Name** <small style="color:gray">Name of the resource</small>
   - Messure <small style="color:gray">The messure unity: *uds* - *l* </small>
  
Also, resources will have relation with itself to know if a resource its crafted from other. We will call it relation **Recipe**.

- **Recipe**:
  - ***ID*** <small style="color:gray">The identifier of the entrie</small>
  - *ID_craft_resource* <small style="color:gray">Foreign key from resource of the resource that would be crafted.</small>
  - *ID_needed_resource* <small style="color:gray">Foreign key from resource of the resource that would be needed to craft the *craft_resource*</small>
  - Cuantity <small style="color:gray">The unity of the needed resource in the recipe of *needed_resource* per unit of *craft_resource*</small>
  

![image of the Models Relation](./design/modles.png)

### 2. Screen Design


In this project, we have like 2 `branch`, one for the storage of the objects information and its update/delete. And the other for make calculous from the storage data.


![Imagen of the screen design](./design/page.png)



### &ensp;&ensp;&ensp;&ensp;&ensp;2.1 Resources

This `branch` start with a list of the resource created. Here you can access to more details or create another.

FOTO LIS

In the details, you can modify the object, delete it, add it to marks or see the recipes.


FOTO DETAILS.


In the recipes you have a table with the elements that compound the object and the cuantities. Here you can access the other objects details, create a new entry of the recipes, modify an entry of the recipes or delete an entry of the recipes

FOTO RECIPES



### &ensp;&ensp;&ensp;&ensp;&ensp;2.2 Calculators 

In this section we have a list of `calculators`

The first one is for resources and calculate the cuantity of resources needed from the recipes.

The other one calculate the amount of energy of the selected generators and its total.

## Intereseting details

1. The messure field in **Resource**, it`s an enum type
2. In the objects app, there is a submodule of python dedicated to the forms, with it own urls.py, views.py and the forms.py.
3. In the resources list, when you change the filter to checkeds, js will make an api request to the server, and it response in a json the resources markers. Also, in the calculators, the js make api request to the django server to take the information of the generators an the recipes of the sources.