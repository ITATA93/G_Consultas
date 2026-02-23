# SQLUser.CT_UOM

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTUOM_RowId | bigint | PK |  | NO | - |
| CTUOM_AllowDecimalQty | varchar |  |  | SI | AllowDecimalQty |
| CTUOM_Code | varchar |  |  | NO | Unit Of Measurement Code |
| CTUOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTUOM_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| CTUOM_CreatedDate | date |  |  | SI | Created Date |
| CTUOM_CreatedTime | time |  |  | SI | Created Time |
| CTUOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTUOM_Desc | varchar |  |  | NO | Unit Of Meauserment Description
HTMLTextBox
Inpu... |
| CTUOM_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| CTUOM_ForeignDesc | varchar |  |  | SI | Foreign Description |
| CTUOM_Owner | varchar |  |  | SI | Owner |
| CTUOM_System | varchar |  |  | SI | System created |
| CTUOM_Type | varchar |  |  | SI | Unit of Measurement Type |
| CTUOM_UpdatedDate | date |  |  | SI | Updated Date |
| CTUOM_UpdatedTime | time |  |  | SI | Updated Time |
| CTUOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | The ability to independently change and control bo... |
| Q04 | - |  |  | SI | The ability to respond meaningfully, in a developm... |
| Q05 | - |  |  | SI | Tolerance of the Skin and Supporting Structure |
| Q06 | - |  |  | SI | Friction: occurs when skin moves against support s... |
| Q07 | - |  |  | SI | Usual diet for age – assess pattern over the most ... |
| Q08 | - |  |  | SI | TISSUE PERFUSION AND OXYGENATION |
| Q09 | - |  |  | SI | Medical Devices |
| Q10 | - |  |  | SI | Any diagnostic or therapeutic device that is curre... |
| Q11 | - |  |  | SI | REPOSITIONABILITY / SKIN PROTECTION |
| Q12 | - |  |  | SI | The Braden QD is a refinement of the Braden Q whic... |
| Q13 | - |  |  | SI | 1. Curley MAQ, Hasbani NR, Quigley SM, et al. Pred... |
| Q14 | - |  |  | SI | 2. Quigley SM, Curley MAQ. Skin Integrity in the P... |
| Q15 | - |  |  | SI | The new Braden QD scale identifies risk for both i... |
| Q16 | - |  |  | SI | MOBILITY |
| Q17 | - |  |  | SI | SENSORY PERCEPTION |
| Q18 | - |  |  | SI | FRICTION & SHEAR |
| Q19 | - |  |  | SI | NUTRITION |
| Q20 | - |  |  | SI | NUMBER of MEDICAL DEVICES |
| Q21 | - |  |  | SI | 3. Bergstom N, Braden BJ, Laguzza A, Holman V. The... |
| Q22 | - |  |  | SI | REPOSITIONABILITY / SKIN PROTECTION |
| Q23 | - |  |  | SI | Any diagnostic or therapeutic device that is curre... |
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