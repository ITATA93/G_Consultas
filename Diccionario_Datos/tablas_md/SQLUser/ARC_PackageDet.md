# SQLUser.ARC_PackageDet

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | ARC_Package Parent Reference |
| DET_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| DET_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| DET_ChargeDifferential | varchar |  |  | SI | Charge Differential |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | DateFrom |
| DET_DateTo | date |  |  | SI | DateTo |
| DET_ExclProportionCalc | varchar |  |  | SI | Exclude for Proportion Calculation |
| DET_ExcludePriorities | varchar |  |  | SI | Exclude Priorities |
| DET_FixedProportionAmount | double |  |  | SI | Fixed Proportion Amount |
| DET_GroupSubGroupLimit | double |  |  | SI | Group/Sub Group Limit Amount |
| DET_LimitQty | double |  |  | SI | LimitQty |
| DET_MainOrder | varchar |  |  | SI | MainOrder |
| DET_Optional | varchar |  |  | SI | Optional |
| DET_OrderItemLimit | double |  |  | SI | Order Item Limit Amount |
| DET_OrderItemLimitPrice | double |  |  | SI | Order Item Limit Price |
| DET_PackageOrderItemPrice | double |  |  | SI | Package Order Item Price |
| DET_PerNewborn | varchar |  |  | SI | Per Newborn |
| DET_PriceOverLimit | double |  |  | SI | PriceOverLimit |
| DET_PriceUnderLimit | double |  |  | SI | PriceUnderLimit |
| DET_RowId | varchar |  |  | NO | - |
| DET_Text1 | varchar |  |  | SI | Text1 |
| DET_Text2 | varchar |  |  | SI | Text2 |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Hora Egreso / Alta |
| Q02 | - |  |  | SI | Estado del Paciente |
| Q03 | - |  |  | SI | Signos Vitales |
| Q04 | - |  |  | SI | Frecuencia Cardiaca |
| Q04ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q05 | - |  |  | SI | Presión Arterial Sistólica |
| Q05ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q06 | - |  |  | SI | Presión Arterial Diastólica |
| Q06ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q07 | - |  |  | SI | Presión Arterial Media |
| Q08 | - |  |  | SI | Frecuencia Respiratoria |
| Q08ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q09 | - |  |  | SI | Saturación O2 |
| Q09ObsDR | - |  |  | SI | Saturación O2 DR |
| Q10 | - |  |  | SI | Hemoglucotest |
| Q10ObsDR | - |  |  | SI | Hemoglucotest  DR |
| Q11 | - |  |  | SI | Escala del Dolor (EVA) |
| Q11ObsDR | - |  |  | SI | Escala del Dolor (EVA) DR |
| Q12 | - |  |  | SI | Entrega Pertenencias Paciente / Acompañante |
| Q13 | - |  |  | SI | Entrega de Exámenes Previos al Paciente/Acompañant... |
| Q14 | - |  |  | SI | Comentarios |
| Q15 | - |  |  | SI | Pertenencias y Accesorios |
| Q16 | - |  |  | SI | Comentarios |
| Q17 | - |  |  | SI | Instrucciones para retiro resultado de biopsia |
| Q18 | - |  |  | SI | Comentarios |
| Q19 | - |  |  | SI | Indicaciones al Alta (verbal o escrita) |
| Q20 | - |  |  | SI | Comentarios |
| Q21 | - |  |  | SI | Responsables |
| Q22 | - |  |  | SI | Médico / Odontólogo |
| Q23 | - |  |  | SI | Enfermera(o) |
| Q24 | - |  |  | SI | TENS / TONS |
| Q25 | - |  |  | SI | Observaciones Generales |
| Q26 | - |  |  | SI | FiO2 |
| Q26ObsDR | - |  |  | SI | FiO2 DR |
| Q27 | - |  |  | SI | Escala de nivel de sedación (Ramsay) |
| Q28 | - |  |  | SI | ALD: Actividad |
| Q28ObsDR | - |  |  | SI | ALD: Actividad DR |
| Q29 | - |  |  | SI | ALD: Respiración |
| Q29ObsDR | - |  |  | SI | ALD: Respiración DR |
| Q30 | - |  |  | SI | ALD: Circulación |
| Q30ObsDR | - |  |  | SI | ALD: Circulación DR |
| Q31 | - |  |  | SI | ALD: Nivel de Consciencia |
| Q31ObsDR | - |  |  | SI | ALD: Nivel de Consciencia DR |
| Q32 | - |  |  | SI | ALD: Saturación de oxígeno |
| Q32ObsDR | - |  |  | SI | ALD: Saturación de oxígeno DR |
| Q33 | - |  |  | SI | ALD: Puntaje |
| Q34 | - |  |  | SI | Escala de Aldrete Modificada |
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