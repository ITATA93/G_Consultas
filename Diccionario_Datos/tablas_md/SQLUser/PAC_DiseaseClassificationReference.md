# SQLUser.PAC_DiseaseClassificationReference

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACDCR_RowID | bigint | PK |  | NO | - |
| PACDCR_ClassificationSystem_DR | bigint |  | FK | SI | Clasification System |
| PACDCR_Code | varchar |  |  | NO | Code |
| PACDCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACDCR_CreatedDate | date |  |  | SI | Created Date |
| PACDCR_CreatedTime | time |  |  | SI | Created Time |
| PACDCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACDCR_DateFrom | date |  |  | SI | Date From |
| PACDCR_DateTo | date |  |  | SI | Date To |
| PACDCR_Desc | varchar |  |  | NO | Description |
| PACDCR_ICD_DR | bigint |  | FK | SI | ICD Reference |
| PACDCR_LOINC_DR | bigint |  | FK | SI | LOINC Reference |
| PACDCR_Owner | varchar |  |  | SI | Owner |
| PACDCR_ParentDisease | varchar |  |  | SI | PACDisease Reference |
| PACDCR_SNOMED_DR | bigint |  | FK | SI | SNOMED Reference |
| PACDCR_UpdatedDate | date |  |  | SI | Updated Date |
| PACDCR_UpdatedTime | time |  |  | SI | Updated Time |
| PACDCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Alertness |
| Q02 | - |  |  | SI | Cooperation |
| Q03 | - |  |  | SI | Auditory comprehension |
| Q04 | - |  |  | SI | Respiration |
| Q05 | - |  |  | SI | Respiratory rate (for swallow) |
| Q06 | - |  |  | SI | Dysphasia |
| Q07 | - |  |  | SI | Dyspraxia |
| Q08 | - |  |  | SI | Dysarthria |
| Q09 | - |  |  | SI | Saliva |
| Q10 | - |  |  | SI | Lip seal |
| Q11 | - |  |  | SI | Tongue movement |
| Q12 | - |  |  | SI | Tongue strength |
| Q13 | - |  |  | SI | Tongue coordination |
| Q14 | - |  |  | SI | Oral preparation |
| Q15 | - |  |  | SI | Gag |
| Q16 | - |  |  | SI | Palate |
| Q17 | - |  |  | SI | Bolus clearance |
| Q18 | - |  |  | SI | Oral transit |
| Q19 | - |  |  | SI | Cough reflex |
| Q20 | - |  |  | SI | Voluntary cough |
| Q21 | - |  |  | SI | Voice |
| Q22 | - |  |  | SI | Tracheostomy |
| Q23 | - |  |  | SI | Pharyngeal phase |
| Q24 | - |  |  | SI | Pharyngeal response |
| Q25 | - |  |  | SI | Diet recommendations |
| Q26 | - |  |  | SI | Fluid recommendation |
| Q27 | - |  |  | SI | Swallow integrity for dysphagia |
| Q28 | - |  |  | SI | Dysphagia |
| Q29 | - |  |  | SI | Aspiration |
| Q30 | - |  |  | SI | Additional problems |
| Q31 | - |  |  | SI | Summary |
| Q32 | - |  |  | SI | Recommendations |
| Q33 | - |  |  | SI | Diagnosis |
| Q34 | - |  |  | SI | Moderate dysphagia: 139 - 167 |
| Q35 | - |  |  | SI | Mild dysphagia: 168 - 177 |
| Q36 | - |  |  | SI | Moderate aspiration: < or equal to 148 |
| Q37 | - |  |  | SI | Mild aspiration: 149 - 169 |
| Q38 | - |  |  | SI | The Mann Assessment of Swallowing Ability (MASA) w... |
| Q39 | - |  |  | SI | Currently, the utility of the MASA has been report... |
| Q40 | - |  |  | SI | In addition, the MASA can quantify the aspiration ... |
| Q41 | - |  |  | SI | The Mann Assessment of Swallowing Ability (MASA) w... |
| Q42 | - |  |  | SI | In addition, the MASA can quantify the aspiration ... |
| Q43 | - |  |  | SI | No dysphagia abnormality: 178 - 200 |
| Q44 | - |  |  | SI | Severe dysphagia : < or = to 138 |
| Q45 | - |  |  | SI | No aspiration abnormatlity : 170 - 200 |
| Q46 | - |  |  | SI | Moderate aspiration : 140 - 148 |
| Q47 | - |  |  | SI | Severe aspiration : < or = 140 |
| Q48 | - |  |  | SI | MASA Score - Dysphagia |
| Q49 | - |  |  | SI | MASA Score - Aspiration |
| Q50 | - |  |  | SI | Swallow integrity for aspiration |
| Q51 | - |  |  | SI | Date |
| Q52 | - |  |  | SI | Time |
| Q53 | - |  |  | SI | MASA Score - Dysphagia |
| Q54 | - |  |  | SI | MASA Score - Aspiration |
| Q55 | - |  |  | SI | Cooperation |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*