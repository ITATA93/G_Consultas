# questionnaire.QTCPREOPANA

> Preoperative Anaesthesia Evaluation

**Schema:** questionnaire
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Preoperative Anaesthesia Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Emergency surgery / procedure |
| Q04 | varchar |  |  | SI | Assessment location |
| Q05 | varchar |  |  | SI | Specify |
| Q06 | varchar |  |  | SI | Planned surgery / procedure |
| Q07 | varchar |  |  | SI | Complication risk of the intervention |
| Q08 | varchar |  |  | SI | Instrument employed to determine the category |
| Q09 | varchar |  |  | SI | Other instrument employed |
| Q10 | varchar |  |  | SI | History of any disease |
| Q11 | varchar |  |  | SI | Positive history for |
| Q12 | varchar |  |  | SI | If Other, please specify |
| Q13 | varchar |  |  | SI | Comments |
| Q14 | varchar |  |  | SI | History of chest pain |
| Q15 | varchar |  |  | SI | History of shortness of breath |
| Q16 | varchar |  |  | SI | Comments on dyspnoea assessment |
| Q17 | varchar |  |  | SI | Presence of pacemaker, ICD or neurostimulator |
| Q18 | varchar |  |  | SI | Perioperative implant management |
| Q19 | varchar |  |  | SI | Medication history reviewed? |
| Q20 | varchar |  |  | SI | Allergies checked? |
| Q21 | varchar |  |  | SI | Alcohol consumption |
| Q22 | varchar |  |  | SI | Pattern of alcohol consumption |
| Q23 | varchar |  |  | SI | Type and quantity |
| Q24 | varchar |  |  | SI | History of tobacco smoking |
| Q25 | varchar |  |  | SI | Type and quantity |
| Q26 | numeric |  |  | SI | Duration of smoking habit (years) |
| Q27 | varchar |  |  | SI | History of recreational drug use |
| Q28 | varchar |  |  | SI | Specify |
| Q29 | date |  |  | SI | Approximate date recreational drugs last used |
| Q30 | varchar |  |  | SI | Quantity of drug last used |
| Q31 | varchar |  |  | SI | Any difficulties with previous anaesthesia? |
| Q32 | varchar |  |  | SI | Details of previous anaesthetic problems |
| Q33 | varchar |  |  | SI | Family history of difficulties with anaesthesia? |
| Q34 | varchar |  |  | SI | Family history of anaesthetic difficulty |
| Q35 | varchar |  |  | SI | Comments on family history of anaesthetic difficul... |
| Q36 | varchar |  |  | SI | Previous transfusions |
| Q37 | varchar |  |  | SI | History of transfusion related reactions |
| Q38 | varchar |  |  | SI | Specify blood products and type of reaction |
| Q39 | varchar |  |  | SI | Acceptability of blood or blood product use |
| Q40 | varchar |  |  | SI | Comments on acceptability of blood or blood produc... |
| Q41 | varchar |  |  | SI | Mallampati |
| Q42 | varchar |  |  | SI | Inter-incisor gap |
| Q43 | varchar |  |  | SI | Thyromental distance |
| Q44 | varchar |  |  | SI | Cervical mobility |
| Q45 | varchar |  |  | SI | Mandibular protrusion |
| Q46 | varchar |  |  | SI | Physical exam performed |
| Q47 | varchar |  |  | SI | Physical exam summary |
| Q48 | varchar |  |  | SI | Reason for physical exam not performed |
| Q49 | varchar |  |  | SI | Previous investigations available and valid |
| Q50 | varchar |  |  | SI | Comments |
| Q51 | varchar |  |  | SI | Evidence of obstructive sleep apnoea syndrome (OSA... |
| Q52 | varchar |  |  | SI | Comments |
| Q53 | varchar |  |  | SI | Antiplatelets agents / anticoagulants in use |
| Q54 | varchar |  |  | SI | Advice given / referral booked |
| Q55 | varchar |  |  | SI | Any other coagulation test required |
| Q56 | varchar |  |  | SI | Describe |
| Q57 | varchar |  |  | SI | Difficult airway management expected |
| Q58 | varchar |  |  | SI | Post-operative admission to ICU planned |
| Q59 | varchar |  |  | SI | Blood / blood products required |
| Q60 | varchar |  |  | SI | Specify |
| Q61 | varchar |  |  | SI | Blood / Blood products requested |
| Q62 | varchar |  |  | SI | Blood / blood products available |
| Q63 | varchar |  |  | SI | ASA |
| Q64 | varchar |  |  | SI | Planned anaesthesia |
| Q65 | varchar |  |  | SI | Consent to anaesthesia obtained |
| Q66 | varchar |  |  | SI | Patient cleared for anaesthesia |
| Q67 | varchar |  |  | SI | Specify additional preparation required |
| Q68 | varchar |  |  | SI | Specify additional preparation required |
| Q69 | varchar |  |  | SI | Comments |
| Q70 | varchar |  |  | SI | Specify additional investigation required |
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