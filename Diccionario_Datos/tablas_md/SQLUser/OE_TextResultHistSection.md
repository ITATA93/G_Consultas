# SQLUser.OE_TextResultHistSection

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HS_ParRef | varchar | PK |  | NO | OE_TextResultHistory Parent Reference |
| HS_Childsub | double |  |  | NO | Childsub |
| HS_HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| HS_HTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| HS_RTFText | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| HS_RowId | varchar |  |  | NO | - |
| HS_TexResSection_DR | varchar |  | FK | SI | Des Ref TexResSection |
| HS_Text | varchar |  |  | SI | Text |
| Q01 | - |  |  | SI | 1. Turning over: Turn over from your back to any s... |
| Q02 | - |  |  | SI | 2. Lying to sitting: Sit on the side of the bed |
| Q03 | - |  |  | SI | 3. Sitting balance: Sit on the edge of the bed wit... |
| Q04 | - |  |  | SI | 4. Sitting to standing: Stand up from your chair (... |
| Q05 | - |  |  | SI | 5. Standing unsupported: Stand without holding on ... |
| Q06 | - |  |  | SI | 6. Transfer: Go from your bed to chair and back ag... |
| Q07 | - |  |  | SI | 7. Walking indoors: Walk for 10 meters in your usu... |
| Q08 | - |  |  | SI | 8. Stairs: Climb up this flight of steps in your u... |
| Q09 | - |  |  | SI | Score 1 (Yes) if the patient can perform the activ... |
| Q10 | - |  |  | SI | Score 0 (No) if the patient cannot |
| Q11 | - |  |  | SI | In case of STROKE patient, please see in Physical ... |
| Q12 | - |  |  | SI | 0 - Unable to perform |
| Q13 | - |  |  | SI | 1 - Assistance of 2 people |
| Q14 | - |  |  | SI | 2 - Assistance of 1 person |
| Q15 | - |  |  | SI | 3 - Requires supervision or verbal instruction |
| Q16 | - |  |  | SI | 4 - Requires an aid or an appliance |
| Q17 | - |  |  | SI | 5 - Independent |
| Q18 | - |  |  | SI | The Modified Rivermead Index evaluates the effecti... |
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