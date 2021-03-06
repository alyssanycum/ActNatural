from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import AnimalEnrichmentItem, Animal, EnrichmentItem, Team, Species, EnrichmentType

@login_required
def animal_enrichment_items_pending_manager_approval(request):

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.all()
    animals = Animal.objects.all()
    species = Species.objects.all()
    enrichment_types = EnrichmentType.objects.all()
    team = Team.objects.get(pk=request.user.employee.team_id)

    # grabs the logged in user's team's animal enrichment items
    team_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if item.animal.team_id == request.user.employee.team_id:
            team_animal_enrichment_items.append(item)

    # grabs the logged in user's team's animal enrichment items that have not been approved by the Manager
    unapproved_team_animal_enrichment_items = []
    for item in team_animal_enrichment_items:
        if item.is_manager_approved == False:
            unapproved_team_animal_enrichment_items.append(item)

    # grabs the associated enrichment item object for each unapproved animal enrichment item
    enrichment_items = []
    for item in unapproved_team_animal_enrichment_items:
        item = EnrichmentItem.objects.get(pk=item.enrichment_item.id)
        enrichment_items.append(item)

    # gets a unique list of those enrichment item objects
    enrichment_items = set(enrichment_items)
    enrichment_items = list(enrichment_items)

    if request.method == 'GET':

        """GETS the animal enrichment items that have been submitted and have not been approved by the Manager yet."""

        if request.user.employee.position == "Manager":

            template = 'animal_enrichment_items/pending_manager_approval.html'
            context = {
                'animals': animals,
                'species': species,
                'enrichment_items': enrichment_items,
                'enrichment_types': enrichment_types,
                'team': team,
                'unapproved_team_animal_enrichment_items': unapproved_team_animal_enrichment_items
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))

    if request.method == 'POST':

        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            """Gets the values from the selected checkboxes and makes a PUT request for each animal enrichment item object that the Manager selected to approve, then re-directs to the items pending manager approval page."""

            selected_items = form_data.getlist('items')

            for item in selected_items:
                animal_enrichment_item = AnimalEnrichmentItem.objects.get(pk=item)
                animal_enrichment_item.animal_id = animal_enrichment_item.animal_id
                animal_enrichment_item.enrichment_item_id = animal_enrichment_item.enrichment_item_id
                animal_enrichment_item.is_manager_approved = True
                animal_enrichment_item.is_vet_approved = animal_enrichment_item.is_vet_approved
                animal_enrichment_item.save()

            return redirect(reverse('actnaturalapp:animal_enrichment_items_pending_manager_approval'))



def animal_enrichment_items_pending_vet_approval(request):

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.all()
    animals = Animal.objects.all()
    species = Species.objects.all()
    enrichment_items = EnrichmentItem.objects.all()
    enrichment_types = EnrichmentType.objects.all()

    # grabs all of the animal enrichment items that have not been approved by the Vet
    unapproved_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if item.is_vet_approved == False:
            unapproved_animal_enrichment_items.append(item)

    # grabs the associated enrichment item object and team object for each unapproved animal enrichment item
    teams = []
    enrichment_items = []
    for item in unapproved_animal_enrichment_items:
        team = item.animal.team.name
        teams.append(team)
        enrichment_item = EnrichmentItem.objects.get(pk=item.enrichment_item.id)
        enrichment_items.append(enrichment_item)

    # gets a unique list of those enrichment item objects
    enrichment_items = set(enrichment_items)
    enrichment_items = list(enrichment_items)

    # gets a unique list of those team objects
    teams = set(teams)
    teams = list(teams)

    if request.method == 'GET':

        """GETS the animal enrichment items that have been submitted and have not been approved by the Vet yet."""

        if request.user.employee.position == "Vet":

            template = 'animal_enrichment_items/pending_vet_approval.html'
            context = {
                'animals': animals,
                'species': species,
                'enrichment_items': enrichment_items,
                'enrichment_types': enrichment_types,
                'teams': teams,
                'unapproved_animal_enrichment_items': unapproved_animal_enrichment_items
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))

    if request.method == 'POST':

        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            """Gets the values from the selected checkboxes and makes a PUT request for each animal enrichment item object that the Vet selected to approve, then re-directs to the items pending vet approval page."""

            selected_items = form_data.getlist('items')

            for item in selected_items:
                animal_enrichment_item = AnimalEnrichmentItem.objects.get(pk=item)
                animal_enrichment_item.animal_id = animal_enrichment_item.animal_id
                animal_enrichment_item.enrichment_item_id = animal_enrichment_item.enrichment_item_id
                animal_enrichment_item.is_manager_approved = animal_enrichment_item.is_manager_approved
                animal_enrichment_item.is_vet_approved = True
                animal_enrichment_item.save()

            return redirect(reverse('actnaturalapp:animal_enrichment_items_pending_vet_approval'))

def animal_enrichment_items_pending_approval(request):

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.all()
    animals = Animal.objects.all()
    enrichment_types = EnrichmentType.objects.all()
    team = Team.objects.get(pk=request.user.employee.team_id)

    # grabs the logged in user's team's animal enrichment items
    team_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if item.animal.team_id == request.user.employee.team_id:
            team_animal_enrichment_items.append(item)

    # grabs the logged in user's team's animal enrichment items that have not been approved by the Manager and/or the Vet
    unapproved_team_animal_enrichment_items = []
    for item in team_animal_enrichment_items:
        if item.is_manager_approved == False or item.is_vet_approved == False:
            unapproved_team_animal_enrichment_items.append(item)

    # grabs the associated enrichment item object and species object for each unapproved animal enrichment item
    enrichment_items = []
    species = []
    for item in unapproved_team_animal_enrichment_items:
        enrichment_item = EnrichmentItem.objects.get(pk=item.enrichment_item.id)
        enrichment_items.append(enrichment_item)
        specie = Species.objects.get(pk=item.animal.species_id)
        species.append(specie)

    # gets a unique list of those enrichment item objects
    enrichment_items = set(enrichment_items)
    enrichment_items = list(enrichment_items)

    # gets a unique list of those species objects
    species = set(species)
    species= list(species)

    if request.method == 'GET':

        """GETS the animal enrichment items that have been submitted and have not been approved by the Manager and/or Vet yet."""

        template = 'animal_enrichment_items/pending_approval.html'
        context = {
            'animals': animals,
            'species': species,
            'enrichment_items': enrichment_items,
            'enrichment_types': enrichment_types,
            'team': team,
            'unapproved_team_animal_enrichment_items': unapproved_team_animal_enrichment_items
        }

        return render(request, template, context)
