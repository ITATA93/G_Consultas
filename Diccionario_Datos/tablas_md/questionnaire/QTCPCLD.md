# questionnaire.QTCPCLD

> Paediatric Criteria Led Discharge

**Schema:** questionnaire
**Columnas:** 202
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Paediatric Criteria Led Discharge

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | EDD on admission |
| Q04 | date |  |  | SI | Revised EDD |
| Q05 | varchar |  |  | SI | Clinical context |
| Q06 | varchar |  |  | SI | Is there any uncertainty about the diagnosis of as... |
| Q07 | varchar |  |  | SI | Has the patient received intravenous (IV) medicati... |
| Q08 | varchar |  |  | SI | Is there a history of Intensive care unit (ICU) ad... |
| Q09 | varchar |  |  | SI | Any chronic respiratory or cardiac condition |
| Q10 | varchar |  |  | SI | Is there any uncertainty about the diagnosis of cr... |
| Q100 | varchar |  |  | SI | Clinician (oral fluids) |
| Q101 | varchar |  |  | SI | Discharge bare weight documented |
| Q102 | varchar |  |  | SI | Weight (kg) |
| Q102ObsDR | varchar |  | FK | SI | Weight (kg) DR |
| Q103 | varchar |  |  | SI | Prescriber (weight) |
| Q104 | varchar |  |  | SI | Criteria status (weight) |
| Q105 | date |  |  | SI | Date (weight) |
| Q106 | time |  |  | SI | Time (weight) |
| Q107 | varchar |  |  | SI | Clinician (weight) |
| Q108 | varchar |  |  | SI | Glasgow Coma Scale 15 |
| Q109 | varchar |  |  | SI | Prescriber (GCS) |
| Q11 | varchar |  |  | SI | Age under 12 months |
| Q110 | varchar |  |  | SI | Criteria status (GCS) |
| Q111 | date |  |  | SI | Date (GCS) |
| Q112 | time |  |  | SI | Time (GCS) |
| Q113 | varchar |  |  | SI | Clinician (GCS) |
| Q114 | varchar |  |  | SI | Headache controlled with simple analgesia |
| Q115 | varchar |  |  | SI | Prescriber (headache controlled) |
| Q116 | varchar |  |  | SI | Criteria status (headache controlled) |
| Q117 | date |  |  | SI | Date (headache controlled) |
| Q118 | time |  |  | SI | Time (headache controlled) |
| Q119 | varchar |  |  | SI | Clinician (headache controlled) |
| Q12 | varchar |  |  | SI | Is this a repeat presentation during this illness |
| Q120 | varchar |  |  | SI | Tolerating oral fluids and no vomiting in previous... |
| Q121 | varchar |  |  | SI | Prescriber (tolerating fluids) |
| Q122 | varchar |  |  | SI | Criteria status (tolerating fluids) |
| Q123 | date |  |  | SI | Date (tolerating fluids) |
| Q124 | time |  |  | SI | Time (tolerating fluids) |
| Q125 | varchar |  |  | SI | Clinician (tolerating fluids) |
| Q126 | varchar |  |  | SI | Additional criteria 1 |
| Q127 | varchar |  |  | SI | Prescriber 1 |
| Q128 | varchar |  |  | SI | Criteria status 1 |
| Q129 | date |  |  | SI | Date 1 |
| Q13 | varchar |  |  | SI | Has this child previously required an Intensive ca... |
| Q130 | time |  |  | SI | Time 1 |
| Q131 | varchar |  |  | SI | Clinician 1 |
| Q132 | varchar |  |  | SI | Additional criteria 2 |
| Q133 | varchar |  |  | SI | Prescriber 2 |
| Q134 | varchar |  |  | SI | Criteria status 2 |
| Q135 | date |  |  | SI | Date 2 |
| Q136 | time |  |  | SI | Time 2 |
| Q137 | varchar |  |  | SI | Clinician 2 |
| Q138 | varchar |  |  | SI | Additional criteria 3 |
| Q139 | varchar |  |  | SI | Prescriber 3 |
| Q14 | varchar |  |  | SI | Could this be tracheitis |
| Q140 | varchar |  |  | SI | Criteria status 3 |
| Q141 | date |  |  | SI | Date 3 |
| Q142 | time |  |  | SI | Time 3 |
| Q143 | varchar |  |  | SI | Clinician 3 |
| Q144 | varchar |  |  | SI | Additional criteria 4 |
| Q145 | varchar |  |  | SI | Prescriber 4 |
| Q146 | varchar |  |  | SI | Criteria status 4 |
| Q147 | date |  |  | SI | Date 4 |
| Q148 | time |  |  | SI | Time 4 |
| Q149 | varchar |  |  | SI | Clinician 4 |
| Q15 | varchar |  |  | SI | Is there any uncertainty about the diagnosis of ga... |
| Q150 | varchar |  |  | SI | Verbal education provided to family |
| Q151 | varchar |  |  | SI | Written patient information provided |
| Q152 | varchar |  |  | SI | Discharge prescription provided (if required) |
| Q153 | varchar |  |  | SI | Discharge letter completed and provided |
| Q154 | varchar |  |  | SI | All observations within normal limits within the l... |
| Q155 | varchar |  |  | SI | Discharge checklist completed |
| Q156 | varchar |  |  | SI | Discharge destination |
| Q157 | varchar |  |  | SI | Discharge checklist notes |
| Q158 | varchar |  |  | SI | I confirm that the criteria have been met and are ... |
| Q159 | varchar |  |  | SI | Consultant name |
| Q16 | varchar |  |  | SI | Age less than 6 months |
| Q160 | varchar |  |  | SI | Reason(s) patient not discharged using criteria le... |
| Q17 | varchar |  |  | SI | Comorbidities e.g. failure to thrive, anaemia, pne... |
| Q18 | varchar |  |  | SI | From a remote Indigenous community |
| Q19 | varchar |  |  | SI | History of chronic gastroenteritis (GI) condition ... |
| Q20 | varchar |  |  | SI | Any cardiovascular or metabolic disease |
| Q21 | varchar |  |  | SI | Does the child have a neurodevelopmental disorder |
| Q22 | varchar |  |  | SI | Does the child have a bleeding disorder |
| Q23 | varchar |  |  | SI | Is there suspicion of non-accidental injury |
| Q24 | varchar |  |  | SI | Is the child &lt;6 months of age |
| Q25 | varchar |  |  | SI | Does the child have a ventricular shunt |
| Q26 | varchar |  |  | SI | Anticipated length of stay &lt;24 hours |
| Q27 | varchar |  |  | SI | Discharge prescription written (if required) |
| Q28 | varchar |  |  | SI | If yes to any of the above, discuss with Paediatri... |
| Q29 | varchar |  |  | SI | Consultant name |
| Q30 | varchar |  |  | SI | Discussion details |
| Q31 | varchar |  |  | SI | Eligibility |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
| Q34 | varchar |  |  | SI | Consultant name |
| Q35 | varchar |  |  | SI | Criteria for discharge |
| Q36 | varchar |  |  | SI | Prescriber |
| Q37 | varchar |  |  | SI | Criteria status |
| Q38 | varchar |  |  | SI | Date |
| Q39 | varchar |  |  | SI | Time |
| Q40 | varchar |  |  | SI | Clinician |
| Q41 | varchar |  |  | SI | Medical review within the last 12 hours |
| Q42 | varchar |  |  | SI | Prescriber (medical review) |
| Q43 | varchar |  |  | SI | Criteria status (medical review) |
| Q44 | date |  |  | SI | Date (medical review) |
| Q45 | time |  |  | SI | Time (medical review) |
| Q46 | varchar |  |  | SI | Clinician (medical review) |
| Q47 | varchar |  |  | SI | Patient observations documented within the last ho... |
| Q48 | varchar |  |  | SI | Prescriber (obs documented) |
| Q49 | varchar |  |  | SI | Criteria status (obs documented) |
| Q50 | date |  |  | SI | Date (obs documented) |
| Q51 | time |  |  | SI | Time (obs documented) |
| Q52 | varchar |  |  | SI | Clinician (obs documented) |
| Q53 | varchar |  |  | SI | Patient/carer(s) demonstrate appropriate spacer te... |
| Q54 | varchar |  |  | SI | Prescriber (spacer demo) |
| Q55 | varchar |  |  | SI | Criteria status (spacer demo) |
| Q56 | date |  |  | SI | Date (spacer demo) |
| Q57 | time |  |  | SI | Time (spacer demo) |
| Q58 | varchar |  |  | SI | Clinician (spacer demo) |
| Q59 | varchar |  |  | SI | Follow up organised (i.e. outpatients / general pr... |
| Q60 | varchar |  |  | SI | Prescriber (FU organized) |
| Q61 | varchar |  |  | SI | Criteria status (FU organized) |
| Q62 | date |  |  | SI | Date (FU organized) |
| Q63 | time |  |  | SI | Time (FU organized) |
| Q64 | varchar |  |  | SI | Clinician (FU organized) |
| Q65 | varchar |  |  | SI | Nil stridor at rest |
| Q66 | varchar |  |  | SI | Prescriber (Nil stridor) |
| Q67 | varchar |  |  | SI | Criteria status (Nil stridor) |
| Q68 | date |  |  | SI | Date (Nil stridor) |
| Q69 | time |  |  | SI | Time (Nil stridor) |
| Q70 | varchar |  |  | SI | Clinician (Nil stridor) |
| Q71 | varchar |  |  | SI | No more than one adrenaline nebuliser given in tot... |
| Q72 | varchar |  |  | SI | Prescriber (one adrenaline nebuliser) |
| Q73 | varchar |  |  | SI | Criteria status (one adrenaline nebuliser) |
| Q74 | date |  |  | SI | Date (one adrenaline nebuliser) |
| Q75 | time |  |  | SI | Time (one adrenaline nebuliser) |
| Q76 | varchar |  |  | SI | Clinician (one adrenaline nebuliser) |
| Q77 | varchar |  |  | SI | No adrenaline nebuliser for at least 4 hours |
| Q78 | varchar |  |  | SI | Prescriber (no adrenaline neb - 4 hrs) |
| Q79 | varchar |  |  | SI | Criteria status (no adrenaline neb - 4 hrs) |
| Q80 | date |  |  | SI | Date (no adrenaline neb - 4 hrs) |
| Q81 | time |  |  | SI | Time (no adrenaline neb - 4 hrs) |
| Q82 | varchar |  |  | SI | Clinician (no adrenaline neb - 4 hrs) |
| Q83 | varchar |  |  | SI | Steroid given |
| Q84 | varchar |  |  | SI | Prescriber (steroid) |
| Q85 | varchar |  |  | SI | Criteria status (steroid) |
| Q86 | date |  |  | SI | Date (steroid) |
| Q87 | time |  |  | SI | Time (steroid) |
| Q88 | varchar |  |  | SI | Clinician (steroid) |
| Q89 | varchar |  |  | SI | Completed oral / NG / IV rehydration |
| Q90 | varchar |  |  | SI | Prescriber (rehydration) |
| Q91 | varchar |  |  | SI | Criteria status (rehydration) |
| Q92 | date |  |  | SI | Date (rehydration) |
| Q93 | time |  |  | SI | Time (rehydration) |
| Q94 | varchar |  |  | SI | Clinician (rehydration) |
| Q95 | varchar |  |  | SI | Hydrated and tolerating oral fluidsHydrated and to... |
| Q96 | varchar |  |  | SI | Prescriber (oral fluids) |
| Q97 | varchar |  |  | SI | Criteria status (oral fluids) |
| Q98 | date |  |  | SI | Date (oral fluids) |
| Q99 | time |  |  | SI | Time (oral fluids) |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*