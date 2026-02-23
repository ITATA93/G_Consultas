# questionnaire.QCLXXBECK

> Inventario de Depresión de Beck (BDI-2)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Inventario de Depresión de Beck (BDI-2)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q22 | varchar |  |  | SI | 0 - 13: minimal depression |
| Q23 | varchar |  |  | SI | 14 - 19: mild depression |
| Q24 | varchar |  |  | SI | 20 - 28: moderate depression |
| Q25 | varchar |  |  | SI | 29 - 63: severe depression |
| Q26 | varchar |  |  | SI | The Beck Depression Inventory BDI is a self-report... |
| Q27 | varchar |  |  | SI | BDI-II contains 21 questions, each answer being sc... |
| QApp | varchar |  |  | SI | Desvalorización |
| QAppe | varchar |  |  | SI | Cambios en el Apetito |
| QCry | varchar |  |  | SI | Llanto |
| QDec | varchar |  |  | SI | Indecisión |
| QDis | varchar |  |  | SI | Pesimismo |
| QDisa | varchar |  |  | SI | Disconformidad con uno mismo |
| QFai | varchar |  |  | SI | Fracaso |
| QGui | varchar |  |  | SI | Sentimientos de Culpa |
| QInt | varchar |  |  | SI | Pérdida de Interés |
| QIrr | varchar |  |  | SI | Agitación |
| QPun | varchar |  |  | SI | Sentimientos de Castigo |
| QSad | varchar |  |  | SI | Tristeza |
| QSat | varchar |  |  | SI | Pérdida de Placer |
| QSex | varchar |  |  | SI | Pérdida de Interés en el Sexo |
| QSle | varchar |  |  | SI | Cambios en los Hábitos de Sueño |
| QSui | varchar |  |  | SI | Pensamientos o Deseos Suicidas |
| QTir | varchar |  |  | SI | Irritabilidad |
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
| QWea | varchar |  |  | SI | Autocrítica |
| QWei | varchar |  |  | SI | Dificultad de Concentración |
| QWor | varchar |  |  | SI | Pérdida de Energía |
| QWorr | varchar |  |  | SI | Cansancio o Fatiga |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*