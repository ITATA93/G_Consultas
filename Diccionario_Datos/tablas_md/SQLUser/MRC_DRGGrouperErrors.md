# SQLUser.MRC_DRGGrouperErrors

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGGE_RowId | bigint | PK |  | NO | - |
| DRGGE_Code | varchar |  |  | NO | Code |
| DRGGE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGGE_CreatedDate | date |  |  | SI | Created Date |
| DRGGE_CreatedTime | time |  |  | SI | Created Time |
| DRGGE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGGE_DateFrom | date |  |  | SI | Date From |
| DRGGE_DateTo | date |  |  | SI | Date To |
| DRGGE_Desc | varchar |  |  | NO | Desfription |
| DRGGE_Owner | varchar |  |  | SI | Owner |
| DRGGE_UpdatedDate | date |  |  | SI | Updated Date |
| DRGGE_UpdatedTime | time |  |  | SI | Updated Time |
| DRGGE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nombre Cuidador |
| Q02 | - |  |  | SI | RUN |
| Q03 | - |  |  | SI | Parentesco |
| Q04 | - |  |  | SI | ¿Piensa que su familiar le pide más ayuda de la qu... |
| Q05 | - |  |  | SI | ¿Piensa que debido al tiempo que dedica a su famil... |
| Q06 | - |  |  | SI | ¿Se siente agobiado por intentar compatibilizar el... |
| Q07 | - |  |  | SI | ¿Siente vergüenza por la conducta de su familiar? |
| Q08 | - |  |  | SI | ¿Se siente enfadado cuando esta cerca de su famili... |
| Q09 | - |  |  | SI | ¿Piensa que el cuidar de su familiar afecta negati... |
| Q10 | - |  |  | SI | ¿Tiene miedo por el futuro de su familiar? |
| Q11 | - |  |  | SI | ¿Piensa que su familiar depende de Ud.? |
| Q12 | - |  |  | SI | ¿Se siente tenso cuando está cerca de su familiar? |
| Q13 | - |  |  | SI | ¿Piensa que su salud ha empeorado debido a tener q... |
| Q14 | - |  |  | SI | ¿Piensa que no tiene tanta intimidad como le gusta... |
| Q15 | - |  |  | SI | ¿Piensa que su vida social se ha visto afectada ne... |
| Q16 | - |  |  | SI | ¿Se siente incómodo por distanciarse de sus amista... |
| Q17 | - |  |  | SI | ¿Piensa que su familiar le considera a usted la ún... |
| Q18 | - |  |  | SI | ¿Piensa que no tiene suficientes ingresos económic... |
| Q19 | - |  |  | SI | ¿Piensa que no será capaz de cuidar a su familiar ... |
| Q20 | - |  |  | SI | ¿Se siente que ha perdido el control de su vida de... |
| Q21 | - |  |  | SI | ¿Desearía poder dejar el cuidado de su familiar a ... |
| Q22 | - |  |  | SI | ¿Se siente indeciso sobre qué hacer con su familia... |
| Q23 | - |  |  | SI | ¿Piensa que debería hacer más por su familiar ? |
| Q24 | - |  |  | SI | ¿Piensa que podría cuidar mejor a su familiar? |
| Q25 | - |  |  | SI | Globalmente, ¿qué grado de carga experimenta por e... |
| QRES | - |  |  | SI | Resultado Test Zarit |
| QRESObsDR | - |  |  | SI | Resultado Test Zarit DR |
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