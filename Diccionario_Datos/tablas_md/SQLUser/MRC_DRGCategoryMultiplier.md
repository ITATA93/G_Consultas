# SQLUser.MRC_DRGCategoryMultiplier

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MULT_ParRef | bigint | PK |  | NO | MRC_DRGCategory Parent Reference |
| MULT_Childsub | double |  |  | NO | Childsub |
| MULT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MULT_CreatedDate | date |  |  | SI | Created Date |
| MULT_CreatedTime | time |  |  | SI | Created Time |
| MULT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MULT_DateFrom | date |  |  | SI | Date From |
| MULT_DateTo | date |  |  | SI | Date To |
| MULT_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| MULT_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| MULT_RowId | varchar |  |  | NO | - |
| MULT_UnderSupplyMultiplier | double |  |  | SI | Under Supply Multiplier |
| MULT_UnderSupplyRatio | double |  |  | SI | Under Supply Ratio |
| MULT_UpdatedDate | date |  |  | SI | Updated Date |
| MULT_UpdatedTime | time |  |  | SI | Updated Time |
| MULT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QCC | - |  |  | SI | Circunferencia cráneo |
| QCD | - |  |  | SI | Conducta |
| QCO | - |  |  | SI | Control cefálico |
| QCS | - |  |  | SI | Consolabilidad |
| QDE | - |  |  | SI | Deglución |
| QDI | - |  |  | SI | Diagnóstico Protocolo de Neurodesarrollo |
| QDIObsDR | - |  |  | SI | Diagnóstico Protocolo de Neurodesarrollo DR |
| QFL | - |  |  | SI | Fija la vista y sigue objeto 90° |
| QHA | - |  |  | SI | Habituación |
| QLL | - |  |  | SI | Llanto |
| QMA | - |  |  | SI | Manos |
| QME | - |  |  | SI | Movimientos de extremidades |
| QMF | - |  |  | SI | Movilidad Facial |
| QMFE | - |  |  | SI | Mira fijamente al examinador |
| QMO | - |  |  | SI | Moro |
| QPE | - |  |  | SI | Peso |
| QPI | - |  |  | SI | Piel |
| QRF | - |  |  | SI | Reacciona frente a ruido fuerte |
| QRP | - |  |  | SI | Rojo pupilar |
| QSD | - |  |  | SI | Se dirige hacia sonido |
| QSS | - |  |  | SI | Sonrisa Social |
| QSU | - |  |  | SI | Succión |
| QTA | - |  |  | SI | Talla |
| QTAX | - |  |  | SI | Tono axial |
| QTO | - |  |  | SI | Tónico - nucal |
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