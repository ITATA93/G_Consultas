# SQLUser.ARC_PayAgreemICDDiagCheck

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICDCK_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| ICDCK_Childsub | double |  |  | NO | Childsub |
| ICDCK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ICDCK_CreatedDate | date |  |  | SI | Created Date |
| ICDCK_CreatedTime | time |  |  | SI | Created Time |
| ICDCK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ICDCK_DateFrom | date |  |  | SI | Date From |
| ICDCK_DateTo | date |  |  | SI | Date To |
| ICDCK_ICDDx_DR | bigint |  | FK | SI | Des Ref ICDCKDx |
| ICDCK_RowId | varchar |  |  | NO | - |
| ICDCK_UpdatedDate | date |  |  | SI | Updated Date |
| ICDCK_UpdatedTime | time |  |  | SI | Updated Time |
| ICDCK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | INSTRUCCIONES: se enumeran una serie de afirmacion... |
| Q02 | - |  |  | SI | Totalmente en Desacuerdo |
| Q03 | - |  |  | SI | Totalmente de acuerdo |
| Q04 | - |  |  | SI | 1 = Totalmente en desacuerdo |
| Q05 | - |  |  | SI | 2 = Algo en desacuerdo |
| Q06 | - |  |  | SI | 3 = Parcialmente de acuerdo |
| Q07 | - |  |  | SI | 4 = Totalmente de acuerdo |
| Q08 | - |  |  | SI | CUESTIONARIO TSK-11SV |
| Q09 | - |  |  | SI | Escala de Tampa para Kinesiofobia |
| Q10 | - |  |  | SI | 1. Tengo miedo de lesionarme si hago ejercicio fís... |
| Q11 | - |  |  | SI | 2. Si me dejara vencer por el dolor, el dolor aume... |
| Q12 | - |  |  | SI | 3. Mi cuerpo me está diciendo que tengo algo serio... |
| Q13 | - |  |  | SI | 4. Tener dolor siempre quiere decir que en el cuer... |
| Q14 | - |  |  | SI | 5. Tengo miedo a lesionarme sin querer. |
| Q15 | - |  |  | SI | 6. Lo más seguro para evitar que aumente el dolor ... |
| Q16 | - |  |  | SI | 7. No me dolería tanto si no tuviese algo serio en... |
| Q17 | - |  |  | SI | 8. El dolor me dice cuándo debo parar la actividad... |
| Q18 | - |  |  | SI | 9. No es seguro para una persona con mi enfermedad... |
| Q19 | - |  |  | SI | 10. No puedo hacer todo lo que la gente normal hac... |
| Q20 | - |  |  | SI | 11. Nadie debería hacer actividades físicas cuando... |
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