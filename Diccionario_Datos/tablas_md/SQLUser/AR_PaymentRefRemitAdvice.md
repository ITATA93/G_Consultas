# SQLUser.AR_PaymentRefRemitAdvice

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RA_ParRef | bigint | PK |  | NO | AR_PaymentRef Parent Reference |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | Responsable de Evaluación |
| Q04 | - |  |  | SI | Aplicación de la prueba |
| Q05 | - |  |  | SI | Otros Motivos |
| Q06 | - |  |  | SI | Lectura : |
| Q07 | - |  |  | SI | Caballo |
| Q08 | - |  |  | SI | Clavel |
| Q09 | - |  |  | SI | Pantalón |
| Q10 | - |  |  | SI | Violín |
| Q11 | - |  |  | SI | ¿Por qué no aplica? |
| Q12 | - |  |  | SI | Total Lectura |
| Q13 | - |  |  | SI | Identificación : |
| Q14 | - |  |  | SI | Caballo |
| Q15 | - |  |  | SI | Clavel |
| Q16 | - |  |  | SI | Pantalón |
| Q17 | - |  |  | SI | Violín |
| Q18 | - |  |  | SI | ¿Por qué no aplica? |
| Q19 | - |  |  | SI | Total Identificación |
| Q20 | - |  |  | SI | Recuerdo Libre : |
| Q21 | - |  |  | SI | Caballo |
| Q22 | - |  |  | SI | Clavel |
| Q23 | - |  |  | SI | Pantalón |
| Q24 | - |  |  | SI | Violín |
| Q25 | - |  |  | SI | ¿Por qué no aplica? |
| Q26 | - |  |  | SI | Total Recuerdo Libre |
| Q27 | - |  |  | SI | Recuerdo con Clave : |
| Q28 | - |  |  | SI | ¿Cuál era el animal? (Caballo) |
| Q29 | - |  |  | SI | ¿Cuál era la flor? (Clavel) |
| Q30 | - |  |  | SI | ¿Cuál era la prenda de vestir?(Pantalón) |
| Q31 | - |  |  | SI | ¿Cuál era el instrumentomusical? (Violín) |
| Q32 | - |  |  | SI | ¿Por qué no aplica? |
| Q33 | - |  |  | SI | Total Recuerdo con Clave |
| Q34 | - |  |  | SI | TOTAL MIS |
| Q35 | - |  |  | SI | Intrusiones |
| Q36 | - |  |  | SI | Observaciones |
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
| RA_Childsub | double |  |  | NO | Childsub |
| RA_Date1 | date |  |  | SI | Date1 |
| RA_Date2 | date |  |  | SI | Date2 |
| RA_Date3 | date |  |  | SI | Date3 |
| RA_Date4 | date |  |  | SI | Date4 |
| RA_Date5 | date |  |  | SI | Date5 |
| RA_Number1 | double |  |  | SI | Number1 |
| RA_Number2 | double |  |  | SI | Number2 |
| RA_Number3 | double |  |  | SI | Number3 |
| RA_Number4 | double |  |  | SI | Number4 |
| RA_Number5 | double |  |  | SI | Number5 |
| RA_RemitAdviceClaim_DR | varchar |  | FK | SI | Des Ref to ARRemittanceAdviceClaim |
| RA_RemittanceAdviceAmount | double |  |  | SI | Remittance Advice Amount |
| RA_RemittanceAdviceDate | date |  |  | SI | Remittance Advice Date |
| RA_RemittanceAdviceTime | time |  |  | SI | Remittance Advice Time |
| RA_RemittanceAdvice_DR | bigint |  | FK | SI | Des Ref Remittance Advice |
| RA_RowId | varchar |  |  | NO | - |
| RA_Text1 | varchar |  |  | SI | Text1 |
| RA_Text2 | varchar |  |  | SI | Text2 |
| RA_Text3 | varchar |  |  | SI | Text3 |
| RA_Text4 | varchar |  |  | SI | Text4 |
| RA_Text5 | varchar |  |  | SI | Text5 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*