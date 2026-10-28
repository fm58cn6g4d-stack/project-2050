"""Reproduce observed elapsed intervals; never treat them as active floor hours."""
from datetime import date,datetime
import json
checks={
 'ARP_resolution_to_signature_calendar_days':(date(2021,3,11)-date(2021,2,5)).days,
 'ARP_motion_to_passage_elapsed_minutes':int((datetime(2021,3,6,12,12)-datetime(2021,3,4,14,35)).total_seconds()/60),
 'ARP_signature_to_CTC_first_disbursement_calendar_days':(date(2021,7,15)-date(2021,3,11)).days,
 'ARP_signature_to_HealthcareGov_assistance_availability_calendar_days':(date(2021,4,1)-date(2021,3,11)).days,
}
assert checks['ARP_resolution_to_signature_calendar_days']==34
assert checks['ARP_motion_to_passage_elapsed_minutes']==45*60+37
assert checks['ARP_signature_to_CTC_first_disbursement_calendar_days']==126
assert checks['ARP_signature_to_HealthcareGov_assistance_availability_calendar_days']==21
print(json.dumps({'status':'observed elapsed-date arithmetic, not forecast calibration','observations':checks},indent=2))
