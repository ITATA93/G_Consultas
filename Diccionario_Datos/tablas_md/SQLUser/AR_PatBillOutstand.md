# SQLUser.AR_PatBillOutstand

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OUTS_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| OUTS_Childsub | double |  |  | NO | Childsub |
| OUTS_CommentOuts | varchar |  |  | SI | Comment Outstanding |
| OUTS_DepartOuts | varchar |  |  | SI | Department Outstanding |
| OUTS_DiscretOutsType_DR | bigint |  | FK | SI | es Ref DiscretOutsType_DR |
| OUTS_EmplNameOuts | varchar |  |  | SI | Empl Name Outstanding |
| OUTS_ExpectedPayDate | date |  |  | SI | ExpectedPayDate |
| OUTS_OutstandAmt | double |  |  | SI | Outstand Amt |
| OUTS_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | Llenado por |
| Q04 | - |  |  | SI | 1. Si usted indica algo al otro lado de la pieza, ... |
| Q05 | - |  |  | SI | 1. Si usted indica algo al otro lado de la pieza, ... |
| Q06 | - |  |  | SI | 2. ¿Alguna vez se ha preguntado si su hijo/a es so... |
| Q07 | - |  |  | SI | 2. ¿Alguna vez se ha preguntado si su hijo/a es so... |
| Q08 | - |  |  | SI | 3. ¿Su hijo/a realiza juegos de fantasía o imagina... |
| Q09 | - |  |  | SI | 3. ¿Su hijo/a realiza juegos de fantasía o imagina... |
| Q10 | - |  |  | SI | 4. ¿A su hijo/a le gusta subirse a cesas? (Por eje... |
| Q11 | - |  |  | SI | 4. ¿A su hijo/a le gusta subirse a cesas? (Profesi... |
| Q12 | - |  |  | SI | 5. ¿Su hijo/a hace movimientos raros con sus dedos... |
| Q13 | - |  |  | SI | 5. ¿Su hijo/a hace movimientos raros con sus dedos... |
| Q14 | - |  |  | SI | 6. ¿Su hijo/a indica o apunta con e dedo cuando qu... |
| Q15 | - |  |  | SI | 6. ¿Su hijo/a indica o apunta con e dedo cuando qu... |
| Q16 | - |  |  | SI | 7. ¿Su hijo/a señala con un dedo cuando quiere mos... |
| Q17 | - |  |  | SI | 7. ¿Su hijo/a señala con un dedo cuando quiere mos... |
| Q18 | - |  |  | SI | 8. ¿Su hijo/a muestra interés en otros niños? (Por... |
| Q19 | - |  |  | SI | 8. ¿Su hijo/a muestra interés en otros niños? (Pro... |
| Q20 | - |  |  | SI | 9. ¿Su hijo/a le muestra cosas acercándoselas o se... |
| Q21 | - |  |  | SI | 9. ¿Su hijo/a le muestra cosas acercándoselas o se... |
| Q22 | - |  |  | SI | 10.¿Su hijo/a responde cuando usted lo llama por s... |
| Q23 | - |  |  | SI | 10.¿Su hijo/a responde cuando usted lo llama por s... |
| Q24 | - |  |  | SI | 11.¿Cuándo usted le sonríe a su hijo./a, él/ella t... |
| Q25 | - |  |  | SI | 11.¿Cuándo usted le sonríe a su hijo./a, él/ella t... |
| Q26 | - |  |  | SI | 12.¿Le molestan a su hijo/a los ruidos comunes? (P... |
| Q27 | - |  |  | SI | 12.¿Le molestan a su hijo/a los ruidos comunes?&nb... |
| Q28 | - |  |  | SI | 13.¿Su hijo/a camina solo? |
| Q29 | - |  |  | SI | 13.¿Su hijo/a camina solo? (Profesional) |
| Q30 | - |  |  | SI | 14.¿Su hijo/a lo mira a los ojos cuando usted le h... |
| Q31 | - |  |  | SI | 14.¿Su hijo/a lo mira a los ojos cuando usted le h... |
| Q32 | - |  |  | SI | 15.¿Su hijo/a imita sus movimientos? (Por ejemplo:... |
| Q33 | - |  |  | SI | 15.¿Su hijo/a imita sus movimientos? (Profesional) |
| Q34 | - |  |  | SI | 16. Si usted se da vuelta a ver algo, ¿su hijo/a t... |
| Q35 | - |  |  | SI | 16 Si usted se da vuelta a ver algo, ¿su hijo/a tr... |
| Q36 | - |  |  | SI | 17.¿Su hijo/a intenta que usted le mire o le prest... |
| Q37 | - |  |  | SI | 17.¿Su hijo/a intenta que usted le mire o le prest... |
| Q38 | - |  |  | SI | 18. ¿Su hijo/a le entiende cuando usted le pide qu... |
| Q39 | - |  |  | SI | 18. ¿Su hijo/a le entiende cuando usted le pide qu... |
| Q40 | - |  |  | SI | 19. Si ocurre algo que llame la atención de su hij... |
| Q41 | - |  |  | SI | 19. Si ocurre algo que llame la atención de su hij... |
| Q42 | - |  |  | SI | 20. ¿Le gustan a su hijo/a los juegos con movimien... |
| Q43 | - |  |  | SI | 20. ¿Le gustan a su hijo/a los juegos con movimien... |
| Q44 | - |  |  | SI | Total M-CHAT (Profesional) |
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