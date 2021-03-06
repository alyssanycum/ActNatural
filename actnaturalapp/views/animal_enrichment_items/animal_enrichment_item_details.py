from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import AnimalEnrichmentItem, Animal, EnrichmentItem


@login_required
def animal_enrichment_item_details(request, animal_enrichment_item_id):

    animal_enrichment_item = AnimalEnrichmentItem.objects.get(pk=animal_enrichment_item_id)
    animal = Animal.objects.get(pk=animal_enrichment_item.animal_id)
    enrichment_item = EnrichmentItem.objects.get(pk=animal_enrichment_item.enrichment_item_id)

    if request.method == 'POST':

        form_data = request.POST

        if (
            "actual_method" in form_data and form_data["actual_method"] == "DELETE"
        ):

            if ("enrichment_page" in form_data):

                """DELETES an animal enrichment item object and then re-directs to the enrichment item's details page."""

                animal_enrichment_item.delete()

                return redirect(reverse('actnaturalapp:enrichment_item', args=[enrichment_item.id]))

            elif ("animal_page" in form_data):

                """DELETES an animal enrichment item object and then re-directs to the animals's details page."""

                animal_enrichment_item.delete()

                return redirect(reverse('actnaturalapp:animal', args=[animal.id]))

            elif ("enrichment_pending_page" in form_data):

                """DELETES an animal enrichment item object and then re-directs to the enrichment item's pending animals page."""

                animal_enrichment_item.delete()

                return redirect(reverse('actnaturalapp:enrichment_item_animals_waiting_approval', args=[enrichment_item.id]))

            elif ("animal_pending_page" in form_data):

                """DELETES an animal enrichment item object and then re-directs to the animals's pending items page."""

                animal_enrichment_item.delete()

                return redirect(reverse('actnaturalapp:animal_enrichment_items_waiting_approval', args=[animal.id]))

            elif ("pending_approval_page" in form_data):

                """DELETES an animal enrichment item object and then re-directs to the pending approvals page."""

                animal_enrichment_item.delete()

                return redirect(reverse('actnaturalapp:animal_enrichment_items_pending_approval'))