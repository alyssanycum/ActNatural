from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem, EnrichmentType, Employee, Team, AnimalEnrichmentItem, Animal, Species


@login_required
def enrichment_item_details(request, enrichment_item_id):

    try:
        enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
    except: 
        return redirect(reverse('actnaturalapp:enrichment_items'))

    employee = Employee.objects.get(pk=request.user.employee.id)
    team = Team.objects.get(pk=enrichment_item.team_id)
    
    enrichment_type = EnrichmentType.objects.get(pk=enrichment_item.enrichment_type_id)

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.filter(enrichment_item_id=enrichment_item.id)

    # sorts the approved and unapproved animal enrichment items into separate lists
    approved_animal_enrichment_items = []
    unapproved_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if (item.is_manager_approved == True & item.is_vet_approved == True):
            approved_animal_enrichment_items.append(item)
        else:
            unapproved_animal_enrichment_items.append(item)

    animals = Animal.objects.all()

    # grabs the associated species object for each approved animal enrichment item
    species = []
    for animal in approved_animal_enrichment_items:
        animal = animal.animal.species.name
        species.append(animal)

    # gets a unique list of those species objects
    species = set(species)
    species = list(species)
    
    if request.method == 'GET':

        """GETS all of a specific enrichment item's details and approved animal enrichment items."""

        if request.user.employee.team_id == enrichment_item.team_id:

            template = 'enrichment_items/enrichment_item_details.html'
            context = {
                "enrichment_item": enrichment_item,
                "enrichment_type": enrichment_type,
                "employee": employee,
                "team": team,
                "approved_animal_enrichment_items": approved_animal_enrichment_items,
                "species": species,
                "animals": animals
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))

    elif request.method == 'POST':

        form_data = request.POST
        form_files = request.FILES

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            if (
                "updated_photo" in form_data
            ):

                """Makes a PUT request to edit a specific enrichment item's image and then re-directs to the enrichment item's details page."""

                enrichment_item.team_id = request.user.employee.team_id
                enrichment_item.enrichment_type_id = enrichment_item.enrichment_type_id
                enrichment_item.name = enrichment_item.name
                enrichment_item.note = enrichment_item.note
                enrichment_item.image = form_files['image']

                enrichment_item.save()

                return redirect(reverse('actnaturalapp:enrichment_item', args=[enrichment_item.id]))

            else:

                """Makes a PUT request to edit a specific enrichment item's details and then re-directs to the enrichment item's details page."""

                enrichment_item.team_id = request.user.employee.team_id
                enrichment_item.enrichment_type_id = form_data['enrichment_type']
                enrichment_item.name = form_data['name']
                enrichment_item.note = form_data['note']
                enrichment_item.image = enrichment_item.image

                enrichment_item.save()

                return redirect(reverse('actnaturalapp:enrichment_item', args=[enrichment_item.id]))
    
        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):

            """DELETES a specific enrichment item and then re-directs to the enrichment items list."""
            
            enrichment_item.delete()

            return redirect(reverse('actnaturalapp:enrichment_items'))

        else:

            """Gets the values from the selected checkboxes and makes a POST request for each animal enrichment item object that the user selected to get approved for a specific enrichment item, then re-directs to the items pending approval page for the enrichment item."""

            selected_animals = form_data.getlist('animals')

            for animal in selected_animals:
                animal_instance = Animal.objects.get(pk=animal)
                new_animal_enrichment_item = AnimalEnrichmentItem.objects.create(
                    animal = animal_instance,
                    enrichment_item = enrichment_item,
                    is_manager_approved = False,
                    is_vet_approved = False
                )

            return redirect(reverse('actnaturalapp:enrichment_item_animals_waiting_approval', args=[enrichment_item.id]))

@login_required
def enrichment_item_animals_waiting_approval(request, enrichment_item_id):

    try:
        enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
    except: 
        return redirect(reverse('actnaturalapp:enrichment_items'))

    employee = Employee.objects.get(pk=request.user.employee.id)
    team = Team.objects.get(pk=enrichment_item.team_id)
    
    enrichment_type = EnrichmentType.objects.get(pk=enrichment_item.enrichment_type_id)

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.filter(enrichment_item_id=enrichment_item.id)

    # sorts the approved and unapproved animal enrichment items into separate lists
    approved_animal_enrichment_items = []
    unapproved_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if (item.is_manager_approved == True & item.is_vet_approved == True):
            approved_animal_enrichment_items.append(item)
        else:
            unapproved_animal_enrichment_items.append(item)

    animals = Animal.objects.all()

    # grabs the associated species object for each approved animal enrichment item
    species = []
    for animal in unapproved_animal_enrichment_items:
        animal = animal.animal.species.name
        species.append(animal)

    # gets a unique list of those species objects
    species = set(species)
    species = list(species)
    
    if request.method == 'GET':

        """GETS all of a specific enrichment item's submitted unapproved animal enrichment items."""

        if request.user.employee.team_id == enrichment_item.team_id:

            template = 'enrichment_items/enrichment_item_animals_waiting_approval.html'
            context = {
                "enrichment_item": enrichment_item,
                "enrichment_type": enrichment_type,
                "employee": employee,
                "team": team,
                "unapproved_animal_enrichment_items": unapproved_animal_enrichment_items,
                "species": species,
                "animals": animals
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))


    