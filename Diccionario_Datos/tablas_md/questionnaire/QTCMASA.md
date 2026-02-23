# questionnaire.QTCMASA

> Mann Assessment of Swallowing Ability (MASA) Score

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mann Assessment of Swallowing Ability (MASA) Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Alertness |
| Q02 | varchar |  |  | SI | Cooperation |
| Q03 | varchar |  |  | SI | Auditory comprehension |
| Q04 | varchar |  |  | SI | Respiration |
| Q05 | varchar |  |  | SI | Respiratory rate (for swallow) |
| Q06 | varchar |  |  | SI | Dysphasia |
| Q07 | varchar |  |  | SI | Dyspraxia |
| Q08 | varchar |  |  | SI | Dysarthria |
| Q09 | varchar |  |  | SI | Saliva |
| Q10 | varchar |  |  | SI | Lip seal |
| Q11 | varchar |  |  | SI | Tongue movement |
| Q12 | varchar |  |  | SI | Tongue strength |
| Q13 | varchar |  |  | SI | Tongue coordination |
| Q14 | varchar |  |  | SI | Oral preparation |
| Q15 | varchar |  |  | SI | Gag |
| Q16 | varchar |  |  | SI | Palate |
| Q17 | varchar |  |  | SI | Bolus clearance |
| Q18 | varchar |  |  | SI | Oral transit |
| Q19 | varchar |  |  | SI | Cough reflex |
| Q20 | varchar |  |  | SI | Voluntary cough |
| Q21 | varchar |  |  | SI | Voice |
| Q22 | varchar |  |  | SI | Tracheostomy |
| Q23 | varchar |  |  | SI | Pharyngeal phase |
| Q24 | varchar |  |  | SI | Pharyngeal response |
| Q25 | varchar |  |  | SI | Diet recommendations |
| Q26 | varchar |  |  | SI | Fluid recommendation |
| Q27 | varchar |  |  | SI | Swallow integrity for dysphagia |
| Q28 | bit |  |  | SI | Dysphagia |
| Q29 | bit |  |  | SI | Aspiration |
| Q30 | varchar |  |  | SI | Additional problems |
| Q31 | varchar |  |  | SI | Summary |
| Q32 | varchar |  |  | SI | Recommendations |
| Q33 | varchar |  |  | SI | Diagnosis |
| Q34 | varchar |  |  | SI | Moderate dysphagia: 139 - 167 |
| Q35 | varchar |  |  | SI | Mild dysphagia: 168 - 177 |
| Q36 | varchar |  |  | SI | Moderate aspiration: < or equal to 148 |
| Q37 | varchar |  |  | SI | Mild aspiration: 149 - 169 |
| Q38 | varchar |  |  | SI | The Mann Assessment of Swallowing Ability (MASA) w... |
| Q39 | varchar |  |  | SI | Currently, the utility of the MASA has been report... |
| Q40 | varchar |  |  | SI | In addition, the MASA can quantify the aspiration ... |
| Q41 | varchar |  |  | SI | The Mann Assessment of Swallowing Ability (MASA) w... |
| Q42 | varchar |  |  | SI | In addition, the MASA can quantify the aspiration ... |
| Q43 | varchar |  |  | SI | No dysphagia abnormality: 178 - 200 |
| Q44 | varchar |  |  | SI | Severe dysphagia : < or = to 138 |
| Q45 | varchar |  |  | SI | No aspiration abnormatlity : 170 - 200 |
| Q46 | varchar |  |  | SI | Moderate aspiration : 140 - 148 |
| Q47 | varchar |  |  | SI | Severe aspiration : < or = 140 |
| Q48 | varchar |  |  | SI | MASA Score - Dysphagia |
| Q49 | varchar |  |  | SI | MASA Score - Aspiration |
| Q50 | varchar |  |  | SI | Swallow integrity for aspiration |
| Q51 | date |  |  | SI | Date |
| Q52 | time |  |  | SI | Time |
| Q53 | varchar |  |  | SI | MASA Score - Dysphagia |
| Q54 | varchar |  |  | SI | MASA Score - Aspiration |
| Q55 | varchar |  |  | SI | Cooperation |
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