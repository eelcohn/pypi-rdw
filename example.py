import json
from rdw.rdw import Rdw

car = Rdw()

apk = car.get_vehicle_data("28ZLT7")
deficiency = car.get_found_deficiencies_data("52FFLK")
recall_status = car.get_recall_status_data("28ZLT7")
added_objects = car.get_added_objects_data("30GXG5")

print("APK Vervaldatum: " + apk[0]["vervaldatum_apk"])

print("Geconstateerde gebreken: " + str(len(deficiency)))
for deficiency in deficiency:
    deficiency_info = car.get_deficiency_data(deficiency["gebrek_identificatie"])
    print("  " + deficiency["gebrek_identificatie"] + ": " + deficiency_info[0]["gebrek_omschrijving"])

print("Openstaande terugroepacties: " + str(len(recall_status)))
for recall in recall_status:
    print("  " + recall["referentiecode_rdw"] + ":")
    recall = car.get_recall_data(recall["referentiecode_rdw"])
    print("    Omschrijving defect: " + recall[0]["omschrijving_defect"])
    recall_risk = car.get_recall_risk_data(recall[0]["referentiecode_rdw"])
    print("    Mogelijk gevaar: " + recall_risk[0]["mogelijk_gevaar"])
    recall_owner_notification = car.get_recall_owner_notification(recall[0]["referentiecode_rdw"])
    print("    Wijze van informeren eigenaar: " + recall_owner_notification[0]["wijze_waarop_u_wordt_ge_nformeerd"])

print("Aantal toegevoegde objecten: " + str(len(recall_status)))
for obj in added_objects:
    print("  " + obj["soort_toe_te_voegen_object_omschrijving"])
