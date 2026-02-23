# questionnaire.QCLXXEDSII

> Escala de Desmoralización (DS-II)

**Schema:** questionnaire
**Columnas:** 59
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Desmoralización (DS-II)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora Evaluación |
| Q03 | varchar |  |  | SI | 1- Siento que tengo pocas cosas buenas para ofrece... |
| Q04 | varchar |  |  | SI | 2. Parece que mi vida no tiene sentido |
| Q05 | varchar |  |  | SI | 3. Siento que mi papel en la vida se ha perdido |
| Q06 | varchar |  |  | SI | 4. Siento que ya no controlo mis emociones |
| Q07 | varchar |  |  | SI | 5. Siento que nadie puede ayudarme |
| Q08 | varchar |  |  | SI | 6. Siento que no puedo ayudarme |
| Q09 | varchar |  |  | SI | 7. Me siento desesperanzado(a) |
| Q10 | varchar |  |  | SI | 8. Me siento irritable |
| Q11 | varchar |  |  | SI | 9. Siento que no afronto bien la vida |
| Q12 | varchar |  |  | SI | 10. Me arrepiento de muchas cosas en la vida |
| Q13 | varchar |  |  | SI | 11. Tiendo a sentirme fácilmente afectado(a) en el... |
| Q14 | varchar |  |  | SI | 12. Me siento afligido/acongojado por lo que me es... |
| Q15 | varchar |  |  | SI | 13. Soy una persona que no vale la pena |
| Q16 | varchar |  |  | SI | 14. Preferiría no estar vivo(a) |
| Q17 | varchar |  |  | SI | 15. Me siento muy solo(a) o aislado(a) |
| Q18 | varchar |  |  | SI | 16. Me siento atrapado(a) por lo que me está pasan... |
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