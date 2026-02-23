# SQLUser.PAC_DischIntentOnAdm

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISINTADM_RowId | bigint | PK |  | NO | - |
| DISINTADM_Code | varchar |  |  | NO | Code |
| DISINTADM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DISINTADM_CreatedDate | date |  |  | SI | Created Date |
| DISINTADM_CreatedTime | time |  |  | SI | Created Time |
| DISINTADM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISINTADM_DateFrom | date |  |  | SI | Date From |
| DISINTADM_DateTo | date |  |  | SI | Date To |
| DISINTADM_Desc | varchar |  |  | NO | Description |
| DISINTADM_Owner | varchar |  |  | SI | Owner |
| DISINTADM_UpdatedDate | date |  |  | SI | Updated Date |
| DISINTADM_UpdatedTime | time |  |  | SI | Updated Time |
| DISINTADM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Thromboembolic risks?	 |
| Q02 | - |  |  | SI | Is one or more risk identified? |
| Q03 | - |  |  | SI | Any contraindications to thromboprophylaxis?	 |
| Q04 | - |  |  | SI | Contraindications to Thrombophylaxis |
| Q05 | - |  |  | SI | Thromboprophylaxis not indicated	 |
| Q06 | - |  |  | SI | Are any contraindications identified?	 |
| Q07 | - |  |  | SI | Discuss with Haematology registrar or consultant	 |
| Q08 | - |  |  | SI | Thromboprophylaxis recommended	 |
| Q09 | - |  |  | SI | Management if prophylaxis recommended |
| Q10 | - |  |  | SI | Is the patient able to self administer Dalteparin? |
| Q11 | - |  |  | SI | Provide the patient with a Dalteparin starter kit ... |
| Q12 | - |  |  | SI | If the patient is unable to self administer the Da... |
| Q13 | - |  |  | SI | *For Patients who not wish to undergo treatment  w... |
| Q14 | - |  |  | SI | The proposed treatment has been discussed with me,... |
| Q15 | - |  |  | SI | Patient given information leaflet	 |
| Q16 | - |  |  | SI | Patient declined information leaflet	 |
| Q17 | - |  |  | SI | Notes |
| Q18 | - |  |  | SI | Patient signature	 |
| Q18UDt | - |  |  | SI | Patient signature	 Last Updated Date |
| Q18UTm | - |  |  | SI | Patient signature	 Last Updated Time |
| Q19 | - |  |  | SI | VTE Prophylaxis for ambulatory patients >16 years ... |
| Q20 | - |  |  | SI | Thromboprophylaxis not indicated |
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