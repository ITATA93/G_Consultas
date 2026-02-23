# SQLUser.MRC_AdditCodeReq

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADDCR_RowId | bigint | PK |  | NO | - |
| ADDCR_Code | varchar |  |  | SI | Code |
| ADDCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADDCR_CreatedDate | date |  |  | SI | Created Date |
| ADDCR_CreatedTime | time |  |  | SI | Created Time |
| ADDCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADDCR_DateFrom | date |  |  | SI | Date From |
| ADDCR_DateTo | date |  |  | SI | Date To |
| ADDCR_Desc | varchar |  |  | SI | Description |
| ADDCR_Owner | varchar |  |  | SI | Owner |
| ADDCR_UpdatedDate | date |  |  | SI | Updated Date |
| ADDCR_UpdatedTime | time |  |  | SI | Updated Time |
| ADDCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. (C) Levanta la cabeza y hombros al ser llevado ... |
| Q02 | - |  |  | SI | 2- (M) Gira la cabeza al sonido de la campanilla |
| Q03 | - |  |  | SI | 3. (LS) Rie a carcajadas * |
| Q04 | - |  |  | SI | 4. (C) La cabeza sigue la cuchara que desaparece |
| Q05 | - |  |  | SI | 5. (M) Camina afirmado de una mano |
| Q06 | - |  |  | SI | 6. (C) Aplaude |
| Q07 | - |  |  | SI | 7. (L) Dice al menos 2 palabras con sentido * |
| Q08 | - |  |  | SI | 8. (LS) Entrega como respuesta a una orden |
| Q09 | - |  |  | SI | 9. (M) Camina Solo |
| Q10 | - |  |  | SI | 10. (C) Espontáneamente garabatea |
| Q11 | - |  |  | SI | 11. (L) Imita tres palabras * |
| Q12 | - |  |  | SI | 12. (LS) Muestra lo que desea, apuntándolo |
| Q13 | - |  |  | SI | 13. (C) Arma una torre de cuatro cubos |
| Q14 | - |  |  | SI | 14. (L) Nombra un objeto de los cuatro presentados |
| Q15 | - |  |  | SI | 15. (M) Se para en un pie con apoyo |
| Q16 | - |  |  | SI | 16. (C) (S) Usa la cuchara |
| Q21 | - |  |  | SI | 21. (M) Se para en un pie sin apoyo 1 segundo |
| Q22 | - |  |  | SI | 22. (C) Desata cordones |
| Q23 | - |  |  | SI | 23. (L) Nombra 2 objetos de los 4 presentados |
| Q24 | - |  |  | SI | 24. (S) Ayuda en tareas simples |
| QDSA12M | - |  |  | SI | Desarrollos Alterados 12 Meses |
| QDSA15M | - |  |  | SI | Desarrollos Alterados 15 Meses |
| QDSA21M | - |  |  | SI | Desarrollos Alterados 21 Meses |
| QDSA24M | - |  |  | SI | Desarrollos Alterados 24 Meses |
| QDSA4M | - |  |  | SI | Desarrollos Alterados 4 Meses |
| QOBS | - |  |  | SI | Observaciones |
| QP12M | - |  |  | SI | Puntaje 12 Meses |
| QP15M | - |  |  | SI | Puntaje 15 Meses |
| QP21M | - |  |  | SI | Puntaje 21 Meses |
| QP24M | - |  |  | SI | Puntaje 24 Meses |
| QP4M | - |  |  | SI | Puntaje 4 Meses |
| QRES12M | - |  |  | SI | Resultado 12 Meses |
| QRES15M | - |  |  | SI | Resultado 15 Meses |
| QRES21M | - |  |  | SI | Resultado 21 Meses |
| QRES24M | - |  |  | SI | Resultado 24 Meses |
| QRES4M | - |  |  | SI | Resultado 4 Meses |
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
| QURR | - |  |  | SI | Resultado Pauta Breve de Desarrollo Psicomotor |
| QURRObsDR | - |  |  | SI | Resultado Pauta Breve de Desarrollo Psicomotor DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*