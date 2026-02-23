# questionnaire.QCLXXEDBECK

> Escala Desesperanza de Beck

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala Desesperanza de Beck

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora Evaluación |
| Q03 | varchar |  |  | SI | Evaluador |
| Q04 | varchar |  |  | SI | Espero el futuro con esperanza y entusiasmo |
| Q05 | varchar |  |  | SI | Puedo darme por vencido, renunciar, ya que no pued... |
| Q06 | varchar |  |  | SI | Cuando las cosas van mal me alivia saber que las n... |
| Q07 | varchar |  |  | SI | No puedo imaginar como sera mi vida dentro de 10 a... |
| Q08 | varchar |  |  | SI | Tengo bastante tiempo para llevar a cabo las cosas... |
| Q09 | varchar |  |  | SI | En el futuro espero poder conseguir los que me pue... |
| Q10 | varchar |  |  | SI | Mi futuro me parece oscuro |
| Q11 | varchar |  |  | SI | Espero mas cosas buenas de la vida que lo que la g... |
| Q12 | varchar |  |  | SI | No logro hacer que las cosas cambien y no existen ... |
| Q13 | varchar |  |  | SI | Mis pasadas experiencias me han preparado bien par... |
| Q14 | varchar |  |  | SI | Todo lo que puedo ver hacia adelante es mas desagr... |
| Q15 | varchar |  |  | SI | No espero conseguir lo que realmente deseo |
| Q16 | varchar |  |  | SI | Cuando miro hacia el futuro espero que sere mas fe... |
| Q17 | varchar |  |  | SI | Las cosas no marchan como quisiera |
| Q18 | varchar |  |  | SI | Tengo una gran confianza en el futuro |
| Q19 | varchar |  |  | SI | Nunca consigo lo que deseo por lo que es absurdo d... |
| Q20 | varchar |  |  | SI | Es muy improbable que pueda lograr una satisfaccio... |
| Q21 | varchar |  |  | SI | El futuro me parece vago e incierto |
| Q22 | varchar |  |  | SI | Espero mas bien epocas buenas que malas |
| Q23 | varchar |  |  | SI | No merece la pena que intente conseguir algo que d... |
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