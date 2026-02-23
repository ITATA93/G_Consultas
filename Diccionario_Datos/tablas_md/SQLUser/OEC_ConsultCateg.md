# SQLUser.OEC_ConsultCateg

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONS_RowId | bigint | PK |  | NO | - |
| CONS_Code | varchar |  |  | NO | Code |
| CONS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONS_CreatedDate | date |  |  | SI | Created Date |
| CONS_CreatedTime | time |  |  | SI | Created Time |
| CONS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONS_DateFrom | date |  |  | SI | DateFrom |
| CONS_DateTo | date |  |  | SI | DateTo |
| CONS_Desc | varchar |  |  | NO | Description |
| CONS_HTML_File1 | varchar |  |  | SI | HTML_File1 |
| CONS_HTML_File2 | varchar |  |  | SI | HTML_File2 |
| CONS_HTML_File3 | varchar |  |  | SI | HTML_File3 |
| CONS_HTML_File_Desc1 | varchar |  |  | SI | HTML_File_Desc1 |
| CONS_HTML_File_Desc2 | varchar |  |  | SI | HTML_File_Desc2 |
| CONS_HTML_File_Desc3 | varchar |  |  | SI | HTML_File_Desc3 |
| CONS_Owner | varchar |  |  | SI | Owner |
| CONS_TemplateAssessment | varchar |  |  | SI | TemplateAssessment |
| CONS_TemplateObjective | varchar |  |  | SI | TemplateObjective |
| CONS_TemplatePlanning | varchar |  |  | SI | TemplatePlanning |
| CONS_TemplateSubjective | varchar |  |  | SI | TemplateSubjective |
| CONS_UpdatedDate | date |  |  | SI | Updated Date |
| CONS_UpdatedTime | time |  |  | SI | Updated Time |
| CONS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Height (cm) |
| Q01ObsDR | - |  |  | SI | Height (cm) DR |
| Q02 | - |  |  | SI | Current weight (kg) |
| Q02ObsDR | - |  |  | SI | Current weight (kg) DR |
| Q03 | - |  |  | SI | Unplanned weight loss in past 3-6 months (kg) |
| Q04 | - |  |  | SI | BMI (kg/m2) |
| Q05 | - |  |  | SI | BMI score |
| Q06 | - |  |  | SI | Unplanned weight loss (%) in past 3-6 months |
| Q07 | - |  |  | SI | Acute disease effect (ADE) |
| Q08 | - |  |  | SI | Weight loss in % |
| Q09 | - |  |  | SI | ADE - Yes, if patient is acutely ill and if there ... |
| Q10 | - |  |  | SI | Acutely ill: Such patients include those who are c... |
| Q11 | - |  |  | SI | 0: Low risk |
| Q12 | - |  |  | SI | 1: Medium risk |
| Q13 | - |  |  | SI | 2: High risk |
| Q14 | - |  |  | SI | MUST is a five-step screening tool to identify adu... |
| Q16 | - |  |  | SI | Estimating BMI category from Mid Upper Arm Circumf... |
| Q17 | - |  |  | SI | The subject's left arm should be bent at the elbow... |
| Q18 | - |  |  | SI | Ask the subject to let arm hang loose and measure ... |
| Q19 | - |  |  | SI | If MUAC is <23.5, BMI is likely to be <20 kg/m2 |
| Q20 | - |  |  | SI |  If MUAC is >32.0 cm, BMI is likely to be >30 kg/m... |
| Q21 | - |  |  | SI | The use of MUAC provides a general indication of B... |
| Q22 | - |  |  | SI | Estimating height from Ulna length	 |
| Q23 | - |  |  | SI | https://www.bapen.org.uk/pdfs/must/must_explan.pdf |
| Q24 | - |  |  | SI | Measure the distance between the bony protrusion o... |
| Q25 | - |  |  | SI | 0 |
| Q26 | - |  |  | SI | Low risk |
| Q27 | - |  |  | SI | 1 |
| Q28 | - |  |  | SI | Medium risk |
| Q29 | - |  |  | SI | 2 - 6 |
| Q30 | - |  |  | SI | High risk |
| Q31 | - |  |  | SI | Score |
| Q32 | - |  |  | SI | Classification |
| Q33 | - |  |  | SI | Date |
| Q34 | - |  |  | SI | Time |
| Q35 | - |  |  | SI | Score |
| Q36 | - |  |  | SI | Score interpretation |
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