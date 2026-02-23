# SQLUser.ARC_PayAgreemDRGDetCPExc

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPEXC_ParRef | varchar | PK |  | NO | ARC_PayAgreemDRGDetails Parent Reference |
| CPEXC_AdmSource | varchar |  |  | SI | AdmSource |
| CPEXC_BillGrp | varchar |  |  | SI | ARCBillGrp |
| CPEXC_Childsub | double |  |  | NO | Childsub |
| CPEXC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CPEXC_CreatedDate | date |  |  | SI | Created Date |
| CPEXC_CreatedTime | time |  |  | SI | Created Time |
| CPEXC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CPEXC_DischDestin | varchar |  |  | SI | DischargeDestination |
| CPEXC_MaxAnaesthDays | double |  |  | SI | Maximum Anaesthetic Records  |
| CPEXC_MaxBillGrpDays | double |  |  | SI | Maximum Billing Group Days |
| CPEXC_MaxItemsAnaestTheatre | double |  |  | SI | Maximum Items per Anaesthetic/Theatre Record |
| CPEXC_MaxRoomTypeDays | double |  |  | SI | Maximum Room Type Days  |
| CPEXC_RevertPerDiemNoTheatre | varchar |  |  | SI | Revert to Per Diem if no Theatre |
| CPEXC_RoomType | varchar |  |  | SI | RoomType |
| CPEXC_RowId | varchar |  |  | NO | - |
| CPEXC_UpdatedDate | date |  |  | SI | Updated Date |
| CPEXC_UpdatedTime | time |  |  | SI | Updated Time |
| CPEXC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha de Evaluación |
| Q02 | - |  |  | SI | 1. Ojos Provocación |
| Q03 | - |  |  | SI | 1. Ojos Severidad |
| Q04 | - |  |  | SI | 1. Ojos Po |
| Q05 | - |  |  | SI | 1. Ojos Total E.M. |
| Q06 | - |  |  | SI | 2. Boca Provocación |
| Q07 | - |  |  | SI | 2. Boca Severidad |
| Q08 | - |  |  | SI | 2. Boca Po |
| Q09 | - |  |  | SI | 2. Boca Total E.M. |
| Q10 | - |  |  | SI | 3. Habla y Deglución Provocación |
| Q11 | - |  |  | SI | 3. Habla y Deglución Severidad |
| Q12 | - |  |  | SI | 3. Habla y Deglución Po |
| Q13 | - |  |  | SI | 3. Habla y Deglución Total E.M. |
| Q14 | - |  |  | SI | 4. Cuello Provocación |
| Q15 | - |  |  | SI | 4. Cuello Severidad |
| Q16 | - |  |  | SI | 4. Cuello Po |
| Q17 | - |  |  | SI | 4. Cuello Total E.M. |
| Q18 | - |  |  | SI | 5. Brazo Derecho Provocación |
| Q19 | - |  |  | SI | 5. Brazo Derecho Severidad |
| Q20 | - |  |  | SI | 5. Brazo Derecho Po |
| Q21 | - |  |  | SI | 5. Brazo Derecho Total  E.M. |
| Q22 | - |  |  | SI | 6. Brazo Izquierdo Provocación |
| Q23 | - |  |  | SI | 6. Brazo Izquierdo Severidad |
| Q24 | - |  |  | SI | 6. Brazo Izquierdo Po |
| Q25 | - |  |  | SI | 6. Brazo Izquierdo Total  E.M. |
| Q26 | - |  |  | SI | 7. Tronco Provocación |
| Q27 | - |  |  | SI | 7. Tronco Severidad |
| Q28 | - |  |  | SI | 7. Tronco Severidad Po |
| Q29 | - |  |  | SI | 7. Tronco Severidad Total E.M. |
| Q30 | - |  |  | SI | 8. Pierna Derecha Provocación |
| Q31 | - |  |  | SI | 8. Pierna Derecha Severidad |
| Q32 | - |  |  | SI | 8. Pierna Derecha Po |
| Q33 | - |  |  | SI | 8. Pierna Derecha Total E.M. |
| Q34 | - |  |  | SI | 9. Pierna Izquierda Provocación |
| Q35 | - |  |  | SI | 9. Pierna Izquierda Severidad |
| Q36 | - |  |  | SI | 9. Pierna Izquierda Po |
| Q37 | - |  |  | SI | 9. Pierna Izquierda Total E.M. |
| Q38 | - |  |  | SI | SUMA PUNTAJE TOTAL  E.M |
| Q39 | - |  |  | SI | CÁLCULO DE PUNTAJE POR ESCALA |
| Q40 | - |  |  | SI | A.ESCALA DE MOVIMIENTO |
| Q41 | - |  |  | SI | B.ESCALA DE DISCAPACIDAD |
| Q42 | - |  |  | SI | 1. Habla |
| Q43 | - |  |  | SI | 2. Escritura |
| Q44 | - |  |  | SI | 3. Alimentación |
| Q45 | - |  |  | SI | 4. Comer/Tragar |
| Q46 | - |  |  | SI | 5. Higiene |
| Q47 | - |  |  | SI | 6. Vestirse |
| Q48 | - |  |  | SI | 7. Caminar |
| Q49 | - |  |  | SI | SUMA PUNTAJE TOTAL  E.D. |
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