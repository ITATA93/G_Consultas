# questionnaire.QFRMPBREVE

> Pauta Breve de Desarrollo Psicomotor

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pauta Breve de Desarrollo Psicomotor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. (C) Levanta la cabeza y hombros al ser llevado ... |
| Q02 | varchar |  |  | SI | 2- (M) Gira la cabeza al sonido de la campanilla |
| Q03 | varchar |  |  | SI | 3. (LS) Rie a carcajadas * |
| Q04 | varchar |  |  | SI | 4. (C) La cabeza sigue la cuchara que desaparece |
| Q05 | varchar |  |  | SI | 5. (M) Camina afirmado de una mano |
| Q06 | varchar |  |  | SI | 6. (C) Aplaude |
| Q07 | varchar |  |  | SI | 7. (L) Dice al menos 2 palabras con sentido * |
| Q08 | varchar |  |  | SI | 8. (LS) Entrega como respuesta a una orden |
| Q09 | varchar |  |  | SI | 9. (M) Camina Solo |
| Q10 | varchar |  |  | SI | 10. (C) Espontáneamente garabatea |
| Q11 | varchar |  |  | SI | 11. (L) Imita tres palabras * |
| Q12 | varchar |  |  | SI | 12. (LS) Muestra lo que desea, apuntándolo |
| Q13 | varchar |  |  | SI | 13. (C) Arma una torre de cuatro cubos |
| Q14 | varchar |  |  | SI | 14. (L) Nombra un objeto de los cuatro presentados |
| Q15 | varchar |  |  | SI | 15. (M) Se para en un pie con apoyo |
| Q16 | varchar |  |  | SI | 16. (C) (S) Usa la cuchara |
| Q21 | varchar |  |  | SI | 21. (M) Se para en un pie sin apoyo 1 segundo |
| Q22 | varchar |  |  | SI | 22. (C) Desata cordones |
| Q23 | varchar |  |  | SI | 23. (L) Nombra 2 objetos de los 4 presentados |
| Q24 | varchar |  |  | SI | 24. (S) Ayuda en tareas simples |
| QDSA12M | varchar |  |  | SI | Desarrollos Alterados 12 Meses |
| QDSA15M | varchar |  |  | SI | Desarrollos Alterados 15 Meses |
| QDSA21M | varchar |  |  | SI | Desarrollos Alterados 21 Meses |
| QDSA24M | varchar |  |  | SI | Desarrollos Alterados 24 Meses |
| QDSA4M | varchar |  |  | SI | Desarrollos Alterados 4 Meses |
| QOBS | varchar |  |  | SI | Observaciones |
| QP12M | varchar |  |  | SI | Puntaje 12 Meses |
| QP15M | varchar |  |  | SI | Puntaje 15 Meses |
| QP21M | varchar |  |  | SI | Puntaje 21 Meses |
| QP24M | varchar |  |  | SI | Puntaje 24 Meses |
| QP4M | varchar |  |  | SI | Puntaje 4 Meses |
| QRES12M | varchar |  |  | SI | Resultado 12 Meses |
| QRES15M | varchar |  |  | SI | Resultado 15 Meses |
| QRES21M | varchar |  |  | SI | Resultado 21 Meses |
| QRES24M | varchar |  |  | SI | Resultado 24 Meses |
| QRES4M | varchar |  |  | SI | Resultado 4 Meses |
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
| QURR | varchar |  |  | SI | Resultado Pauta Breve de Desarrollo Psicomotor |
| QURRObsDR | varchar |  | FK | SI | Resultado Pauta Breve de Desarrollo Psicomotor DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*