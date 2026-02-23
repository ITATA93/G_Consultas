# SQLUser.ARC_PayAgreemLocAgr

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGR_ParRef | varchar | PK |  | NO | ARC_PayAgreemLocation Parent Reference |
| AGR_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| AGR_Childsub | double |  |  | NO | Childsub |
| AGR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AGR_CreatedDate | date |  |  | SI | Created Date |
| AGR_CreatedTime | time |  |  | SI | Created Time |
| AGR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AGR_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| AGR_RowId | varchar |  |  | NO | - |
| AGR_UpdatedDate | date |  |  | SI | Updated Date |
| AGR_UpdatedTime | time |  |  | SI | Updated Time |
| AGR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | A. Alimentación |
| Q02 | - |  |  | SI | B. Aseo Menor |
| Q03 | - |  |  | SI | C. Aseo Mayor |
| Q04 | - |  |  | SI | D. Vestuario Cuerpo Superior |
| Q05 | - |  |  | SI | E. Vestuario Cuerpo Inferior |
| Q06 | - |  |  | SI | F. Aseo Perineal |
| Q07 | - |  |  | SI | G. Manejo Vesical |
| Q08 | - |  |  | SI | H. Manejo Intestinal |
| Q09 | - |  |  | SI | I. Cama - Silla |
| Q10 | - |  |  | SI | J. WC |
| Q11 | - |  |  | SI | K. Tina o Ducha |
| Q12 | - |  |  | SI | L. Marcha/Silla de Ruedas |
| Q13 | - |  |  | SI | M. Escalas |
| Q14 | - |  |  | SI | N. Comprensión |
| Q15 | - |  |  | SI | O. Expresión |
| Q16 | - |  |  | SI | P. Interacción Social |
| Q17 | - |  |  | SI | Q. Solución de Problemas |
| Q18 | - |  |  | SI | R. Memoria |
| Q19 | - |  |  | SI | Autocuidado |
| Q20 | - |  |  | SI | Control Esfinteriano |
| Q21 | - |  |  | SI | Transferencias |
| Q22 | - |  |  | SI | Locomoción |
| Q23 | - |  |  | SI | Comunicación |
| Q24 | - |  |  | SI | Cognición Social |
| Q25 | - |  |  | SI | Motor |
| Q26 | - |  |  | SI | Cognitivo |
| Q27 | - |  |  | SI | Resultado Escala de FIM |
| Q27ObsDR | - |  |  | SI | Resultado Escala de FIM DR |
| Q28 | - |  |  | SI | Autocuidado |
| Q29 | - |  |  | SI | Control Esfinteriano |
| Q30 | - |  |  | SI | Transferencias |
| Q31 | - |  |  | SI | Locomoción |
| Q32 | - |  |  | SI | Comunicación |
| Q33 | - |  |  | SI | Cognición Social |
| Q34 | - |  |  | SI | SUB - ESCALAS |
| Q35 | - |  |  | SI | DOMINIO |
| Q36 | - |  |  | SI | GRADO DE DEPENDENCIA |
| Q37 | - |  |  | SI | Sin Ayuda |
| Q38 | - |  |  | SI | Dependencia Modificada |
| Q39 | - |  |  | SI | Dependencia Completa |
| Q40 | - |  |  | SI | NIVEL DE FUNCIONALIDAD |
| Q41 | - |  |  | SI | 7. Independencia completa |
| Q42 | - |  |  | SI | 6. Independencia modificada |
| Q43 | - |  |  | SI | 5. Supervisión |
| Q44 | - |  |  | SI | 4. Asistencia mínima (mayor 75% independencia) |
| Q45 | - |  |  | SI | 3. Asistencia moderada (mayor 50% independencia) |
| Q46 | - |  |  | SI | 2. Asistencia máxima (mayor 25% independencia) |
| Q47 | - |  |  | SI | 1. Asistencia total (menor 25% independencia) |
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