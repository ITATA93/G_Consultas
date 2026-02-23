# SQLUser.ARC_ItemPartialKeywords

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PKEYW_RowId | bigint | PK |  | NO | - |
| PKEYW_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| PKEYW_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| PKEYW_Agent_DR | bigint |  | FK | SI | Des Ref MHCAgent |
| PKEYW_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| PKEYW_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| PKEYW_CreatedDate | date |  |  | SI | Created Date |
| PKEYW_CreatedTime | time |  |  | SI | Created Time |
| PKEYW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PKEYW_Desc | varchar |  |  | SI | Description |
| PKEYW_GenKey | varchar |  |  | SI | GenKey |
| PKEYW_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| PKEYW_INCI_DR | bigint |  | FK | SI | Des Ref INCI |
| PKEYW_Keyword | varchar |  |  | SI | Keyword |
| PKEYW_OrderCateg_DR | bigint |  | FK | SI | Des Ref OrderCateg |
| PKEYW_OrderSubCat_DR | bigint |  | FK | SI | Des Ref OrderSubCat |
| PKEYW_Region | varchar |  |  | SI | Region |
| PKEYW_TransferDestination_DR | bigint |  | FK | SI | Des Ref PACTransferDestination |
| PKEYW_Type | varchar |  |  | SI | Type |
| PKEYW_UpdatedDate | date |  |  | SI | Updated Date |
| PKEYW_UpdatedTime | time |  |  | SI | Updated Time |
| PKEYW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PKEYW_Vendor_DR | bigint |  | FK | SI | Des Ref Vendor |
| Q02 | - |  |  | SI | Pje. Glasgow (Adultos) |
| Q02ObsDR | - |  |  | SI | Pje. Glasgow (Adultos) DR |
| Q05 | - |  |  | SI | Temperatura Axilar |
| Q05ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q07 | - |  |  | SI | Presión Arterial Media |
| Q07ObsDR | - |  |  | SI | Presión Arterial Media DR |
| Q08 | - |  |  | SI | Frecuencia Cardiaca |
| Q08ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q09 | - |  |  | SI | Frecuencia Respiratoria |
| Q09ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q10 | - |  |  | SI | FiO2 |
| Q10ObsDR | - |  |  | SI | FiO2 DR |
| Q11 | - |  |  | SI | PaO2 |
| Q11ObsDR | - |  |  | SI | PaO2 DR |
| Q12 | - |  |  | SI | PaCO2 |
| Q12ObsDR | - |  |  | SI | PaCO2 DR |
| Q13 | - |  |  | SI | Presión Atmosférica |
| Q13ObsDR | - |  |  | SI | Presión Atmosférica DR |
| Q14 | - |  |  | SI | Ph Arterial |
| Q14ObsDR | - |  |  | SI | Ph Arterial DR |
| Q15 | - |  |  | SI | Sodio Sérico |
| Q15ObsDR | - |  |  | SI | Sodio Sérico DR |
| Q16 | - |  |  | SI | Potasio Sérico |
| Q16ObsDR | - |  |  | SI | Potasio Sérico DR |
| Q17 | - |  |  | SI | Creatinina Sérica |
| Q17ObsDR | - |  |  | SI | Creatinina Sérica DR |
| Q18 | - |  |  | SI | Falla Renal Aguida |
| Q19 | - |  |  | SI | Hematocrito |
| Q19ObsDR | - |  |  | SI | Hematocrito DR |
| Q20 | - |  |  | SI | Recuento de Leucocitos |
| Q20ObsDR | - |  |  | SI | Recuento de Leucocitos DR |
| Q22 | - |  |  | SI | Clasificación de la Admisión |
| Q23 | - |  |  | SI | Puntaje APACHE II |
| Q23ObsDR | - |  |  | SI | Puntaje APACHE II DR |
| Q24 | - |  |  | SI | Conversión a Mortalidad |
| Q24ObsDR | - |  |  | SI | Conversión a Mortalidad DR |
| Q26 | - |  |  | SI | Categoría de Diagnóstico de Admisión UCI (No Opera... |
| Q27 | - |  |  | SI | Categoría de Diagnóstico de Admisión UCI (Operator... |
| Q28 | - |  |  | SI | Paciente Requirió Cirugía de Emergencia |
| Q29 | - |  |  | SI | Edad (Años) |
| Q30 | - |  |  | SI | Insuficiencia Orgánica Sistémica Severa o Paciente... |
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