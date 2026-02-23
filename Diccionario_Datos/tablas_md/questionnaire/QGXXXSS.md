# questionnaire.QGXXXSS

> CheckList Quirúrgico (First Edition)

**Schema:** questionnaire
**Columnas:** 186
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* CheckList Quirúrgico (First Edition)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Before Induction of Anaesthesia |
| Q02 | date |  |  | SI | Sign in |
| Q03 | varchar |  |  | SI | Patient has confirmed |
| Q04 | bit |  |  | SI | Identity |
| Q05 | bit |  |  | SI | Site marked |
| Q06 | bit |  |  | SI | Procedure |
| Q07 | bit |  |  | SI | Consent |
| Q08 | varchar |  |  | SI | Site marked |
| Q09 | bit |  |  | SI | Check equipamiento de anestesia completado |
| Q10 | bit |  |  | SI | Pulse oximeter on patient and functioning |
| Q100 | varchar |  |  | SI | Present necessary consents |
| Q101 | varchar |  |  | SI | Anaesthesia Equipment Check Completed |
| Q102 | varchar |  |  | SI | Pulse oximeter and ECG on patient |
| Q103 | varchar |  |  | SI | Identification of known allergy risks |
| Q104 | varchar |  |  | SI | Difficulty in managing the airways or risk of aspi... |
| Q105 | varchar |  |  | SI | Limitations to the required position |
| Q106 | varchar |  |  | SI | The risk of blood loss was assessed (> 500ml or> 7... |
| Q107 | varchar |  |  | SI | Check team |
| Q108 | varchar |  |  | SI | Surgeon, anesthetist and nurses confirmed: the pat... |
| Q109 | varchar |  |  | SI | Has antibiotic prophylaxis been give within the la... |
| Q11 | varchar |  |  | SI | Essential equipment available |
| Q110 | varchar |  |  | SI | Statement by the surgeon on duration of surgery, r... |
| Q111 | varchar |  |  | SI | Statement by the anesthetist on patient specificit... |
| Q112 | varchar |  |  | SI | Verification by the nurse about the availability o... |
| Q113 | varchar |  |  | SI | Any essential radiological imaging available? |
| Q114 | varchar |  |  | SI | Confirm name of procedure performed |
| Q115 | varchar |  |  | SI | The final count of gauzes, scalpels, needles and o... |
| Q116 | varchar |  |  | SI | The specimen is labelled (including patient name) |
| Q117 | varchar |  |  | SI | Correct registration of the implanted prosthetic m... |
| Q118 | varchar |  |  | SI | The team reviewed the important and critical aspec... |
| Q119 | varchar |  |  | SI | Reporting any problems connected to the equipment |
| Q12 | varchar |  |  | SI | Does the patient have a known allergy? |
| Q120 | varchar |  |  | SI | The postoperative plan for DVT prophylaxis, antibi... |
| Q121 | varchar |  |  | SI | Equipment and prosthesis available |
| Q124 | varchar |  |  | SI | Identity |
| Q125 | varchar |  |  | SI | Site marked |
| Q126 | varchar |  |  | SI | Procedure |
| Q127 | varchar |  |  | SI | Consent |
| Q128 | varchar |  |  | SI | Pulse oximeter on patient and functioning |
| Q129 | varchar |  |  | SI | Confirm all team members have introduced themselve... |
| Q13 | varchar |  |  | SI | Does the patient have a known difficult airway or ... |
| Q130 | varchar |  |  | SI | Surgeon, anaesthesia professional and nurse verbal... |
| Q131 | varchar |  |  | SI | Correct patient |
| Q132 | varchar |  |  | SI | Correct site and side of procedure |
| Q133 | varchar |  |  | SI | Correct procedure |
| Q134 | varchar |  |  | SI | Nurse confirm with the team the name of the proced... |
| Q135 | varchar |  |  | SI | Surgeon, anaesthesia professional and nurse review... |
| Q136 | varchar |  |  | SI | That instrument, sponge and needle counts are corr... |
| Q137 | varchar |  |  | SI | Surgeon reviews: what are the critical or unexpect... |
| Q138 | varchar |  |  | SI | Anaesthesia team reviews: are there any patient - ... |
| Q139 | varchar |  |  | SI | Nursing team reviews: has sterility (including ind... |
| Q14 | varchar |  |  | SI | Does the patient have a known risk of >500ml blood... |
| Q140 | varchar |  |  | SI | Has the patient confirmed his/her identity, site, ... |
| Q141 | varchar |  |  | SI | Has the position of the patient at surgery been pr... |
| Q142 | varchar |  |  | SI | Does the patient have a known difficult airway or ... |
| Q143 | varchar |  |  | SI | Operation number |
| Q144 | varchar |  |  | SI | Operation / Procedure |
| Q145 | varchar |  |  | SI | Essential equipment available |
| Q15 | varchar |  |  | SI | Before skin incision |
| Q16 | date |  |  | SI | Time out |
| Q17 | bit |  |  | SI | Confirm all team members have introduced themselve... |
| Q18 | bit |  |  | SI | Surgeon, anaesthesia professional and nurse verbal... |
| Q19PROFESSIONAL | bit |  |  | SI | Correct patient |
| Q20PROFESSIONAL | bit |  |  | SI | Correct site and side of procedure |
| Q21PROFESSIONAL | bit |  |  | SI | Correct procedure |
| Q22 | varchar |  |  | SI | Anticipated critical events |
| Q22a | varchar |  |  | SI | Anticipated critical events |
| Q23 | varchar |  |  | SI | Has antibiotic prophylaxis been give within the la... |
| Q24 | varchar |  |  | SI | Is essential imaging displayed? |
| Q25 | varchar |  |  | SI | Before patient leaves operation room |
| Q26 | date |  |  | SI | Sign out |
| Q27 | varchar |  |  | SI | Nurse verbally confirms with the team |
| Q28 | bit |  |  | SI | Nurse confirm with the team the name of the proced... |
| Q29 | varchar |  |  | SI | Completion of instrument, sponge and needle counts |
| Q30 | varchar |  |  | SI | Specimen labelling (read specimen labels aloud, in... |
| Q31 | varchar |  |  | SI | Whether There Are Any Equipament Problems To Be Ad... |
| Q32 | bit |  |  | SI | Surgeon, anaesthesia professional and nurse review... |
| Q33 | varchar |  |  | SI | Nurse verbally confirms with the team |
| Q34 | bit |  |  | SI | That instrument, sponge and needle counts are corr... |
| Q35 | time |  |  | SI | Sign in time |
| Q36 | time |  |  | SI | Time out time |
| Q37 | bit |  |  | SI | Surgeon reviews: what are the critical or unexpect... |
| Q38 | varchar |  |  | SI | Are there equipment issues or any concerns |
| Q39 | time |  |  | SI | Sign out time |
| Q40 | bit |  |  | SI | Anaesthesia team reviews: are there any patient-sp... |
| Q41 | bit |  |  | SI | Nursing Team Reviews: Has Sterility (Including Ind... |
| Q42 | varchar |  |  | SI | Any essential radiological imaging available? |
| Q43 | varchar |  |  | SI | All surgical equipment & prosthesis checked and av... |
| Q44 | varchar |  |  | SI | Any known alerts? |
| Q45 | varchar |  |  | SI | Blood availability? |
| Q45a | varchar |  |  | SI | Blood availability? |
| Q46 | varchar |  |  | SI | Sign in completed by |
| Q47 | time |  |  | SI | Sign in time |
| Q48 | date |  |  | SI | Sign in date |
| Q49 | varchar |  |  | SI | Sign in complete |
| Q50 | varchar |  |  | SI | Patient positioned correctly and safely |
| Q51 | varchar |  |  | SI | All essential monitoring applied and functioning |
| Q52 | varchar |  |  | SI | Venous thromboprophylaxis? |
| Q53 | varchar |  |  | SI | Sterility confirmed |
| Q54 | varchar |  |  | SI | Equipment and prosthesis available |
| Q55 | varchar |  |  | SI | Critical events / Concerns notes |
| Q56 | varchar |  |  | SI | Time out completed by |
| Q57 | time |  |  | SI | Time out time |
| Q58 | date |  |  | SI | Time out date |
| Q59 | varchar |  |  | SI | Time out complete |
| Q60 | varchar |  |  | SI | Any radiological imaging, personal effects and any... |
| Q61 | varchar |  |  | SI | Comments |
| Q62 | varchar |  |  | SI | Sign out completed by |
| Q63 | time |  |  | SI | Sign out time |
| Q64 | date |  |  | SI | Sign out date |
| Q65 | varchar |  |  | SI | Sign out complete |
| Q66 | varchar |  |  | SI | The instrument, sponge and sharps are correct? |
| Q67 | varchar |  |  | SI | The specimen is labelled (including patient name) |
| Q68 | varchar |  |  | SI | Whether there are any equipment problems to be add... |
| Q69 | varchar |  |  | SI | Pre anaesthesia assessment |
| Q70 | varchar |  |  | SI | In case under LA procedure |
| Q71 | varchar |  |  | SI | Antibiotic prophylaxis with 60 - 120 min. before i... |
| Q72 | time |  |  | SI | Time administered |
| Q73 | varchar |  |  | SI | Sterilization indicators have been confirmed |
| Q74 | varchar |  |  | SI | Surgical fire risk assessment |
| Q75 | varchar |  |  | SI | Notes |
| Q76 | varchar |  |  | SI | Second care provider signature |
| Q77 | bit |  |  | SI | Has the patient confirmed his/her identity, site, ... |
| Q78 | varchar |  |  | SI | Post - operative bed booked |
| Q79 | varchar |  |  | SI | Surgeon reviews: what are the critical or unexpect... |
| Q80 | varchar |  |  | SI | Anaesthesia team reviews: are there any patient-sp... |
| Q81 | varchar |  |  | SI | Nursing team reviews: has sterility (including ind... |
| Q82 | varchar |  |  | SI | Venous thromboprophylaxis? |
| Q83 | varchar |  |  | SI | Sign in surgeon |
| Q84 | varchar |  |  | SI | Sign in anaesthetist |
| Q85 | varchar |  |  | SI | To be completed with at least nurse, anaesthetist ... |
| Q86 | varchar |  |  | SI | Surgeon, anaesthesia professional and nurse verbal... |
| Q87 | varchar |  |  | SI | Has antibiotic prophylaxis been given within the l... |
| Q88 | varchar |  |  | SI | Time out surgeon |
| Q89 | varchar |  |  | SI | Time out anaesthetist |
| Q90 | varchar |  |  | SI | To be completed with at least nurse, anaesthetist ... |
| Q91 | varchar |  |  | SI | Sign out surgeon |
| Q92 | varchar |  |  | SI | Sign out anaesthetist |
| Q93 | varchar |  |  | SI | To be completed with at least nurse and anaestheti... |
| Q94 | varchar |  |  | SI | Nurse confirms verbally with the team |
| Q95 | date |  |  | SI | Date |
| Q96 | time |  |  | SI | Time |
| Q97 | varchar |  |  | SI | Anticipated critical events |
| Q98 | varchar |  |  | SI | Patient has confirmed |
| Q99 | varchar |  |  | SI | The patient confirmed: identity, surgery site, sur... |
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