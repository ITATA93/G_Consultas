# SQLUser.AR_PatBillCredit

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRED_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| CRED_ARPBL_DR | bigint |  | FK | SI | Des Ref ARPatientBill |
| CRED_AccountPeriod_DR | bigint |  | FK | SI | Des Ref AccountPeriod |
| CRED_Childsub | double |  |  | NO | Childsub |
| CRED_Comments | varchar |  |  | SI | Comments |
| CRED_CreditAmt | double |  |  | SI | Credit Amt |
| CRED_Date | date |  |  | SI | Date |
| CRED_InActive | varchar |  |  | SI | InActive |
| CRED_RowId | varchar |  |  | NO | - |
| CRED_Text1 | varchar |  |  | SI | Department |
| CRED_Text2 | varchar |  |  | SI | Employee |
| CRED_Time | time |  |  | SI | Time |
| CRED_User_DR | bigint |  | FK | SI | Des Ref User |
| CRED_WOReason_DR | bigint |  | FK | SI | Des Ref WO Reason |
| Q22 | - |  |  | SI | 0 - 13: minimal depression |
| Q23 | - |  |  | SI | 14 - 19: mild depression |
| Q24 | - |  |  | SI | 20 - 28: moderate depression |
| Q25 | - |  |  | SI | 29 - 63: severe depression |
| Q26 | - |  |  | SI | The Beck Depression Inventory BDI is a self-report... |
| Q27 | - |  |  | SI | BDI-II contains 21 questions, each answer being sc... |
| QApp | - |  |  | SI | Desvalorización |
| QAppe | - |  |  | SI | Cambios en el Apetito |
| QCry | - |  |  | SI | Llanto |
| QDec | - |  |  | SI | Indecisión |
| QDis | - |  |  | SI | Pesimismo |
| QDisa | - |  |  | SI | Disconformidad con uno mismo |
| QFai | - |  |  | SI | Fracaso |
| QGui | - |  |  | SI | Sentimientos de Culpa |
| QInt | - |  |  | SI | Pérdida de Interés |
| QIrr | - |  |  | SI | Agitación |
| QPun | - |  |  | SI | Sentimientos de Castigo |
| QSad | - |  |  | SI | Tristeza |
| QSat | - |  |  | SI | Pérdida de Placer |
| QSex | - |  |  | SI | Pérdida de Interés en el Sexo |
| QSle | - |  |  | SI | Cambios en los Hábitos de Sueño |
| QSui | - |  |  | SI | Pensamientos o Deseos Suicidas |
| QTir | - |  |  | SI | Irritabilidad |
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
| QWea | - |  |  | SI | Autocrítica |
| QWei | - |  |  | SI | Dificultad de Concentración |
| QWor | - |  |  | SI | Pérdida de Energía |
| QWorr | - |  |  | SI | Cansancio o Fatiga |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*