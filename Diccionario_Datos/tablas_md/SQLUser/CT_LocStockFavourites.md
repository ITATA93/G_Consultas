# SQLUser.CT_LocStockFavourites

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STF_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| Q01 | - |  |  | SI | MENARQUIA |
| Q02 | - |  |  | SI | MENOPAUSIA |
| Q03 | - |  |  | SI | Terapia de Reemplazo Hormonal |
| Q04 | - |  |  | SI | Ciclo |
| Q05 | - |  |  | SI | Frecuencia del ciclo |
| Q06 | - |  |  | SI | Duración |
| Q07 | - |  |  | SI | FUR |
| Q08 | - |  |  | SI | Observaciones Ciclo Menstrual |
| Q09 | - |  |  | SI | Edad de inicio |
| Q10 | - |  |  | SI | Actividad Actual |
| Q11 | - |  |  | SI | Método Anticonceptivo |
| Q12 | - |  |  | SI | Fecha último PAP |
| Q13 | - |  |  | SI | Resultado PAP |
| Q14 | - |  |  | SI | Observaciones PAP |
| Q15 | - |  |  | SI | Fecha última mamografía |
| Q16 | - |  |  | SI | Resultado Mamografía |
| Q17 | - |  |  | SI | ¿Requirió ECO Mamaria complementaria? |
| Q18 | - |  |  | SI | Resultado ECO mamaria |
| Q19 | - |  |  | SI | Observaciones ECO Mamaria |
| Q20 | - |  |  | SI | Observaciones Mamografia |
| Q21 | - |  |  | SI | Observaciones Actividad Sexual |
| Q22 | - |  |  | SI | Numero de parejas sexuales |
| Q23 | - |  |  | SI | Conducta sexual de riesgo |
| Q24 | - |  |  | SI | Desea agregar observaciones? (Ciclo Menstrual) |
| Q25 | - |  |  | SI | Desea agregar observaciones? (Actividad Sexual) |
| Q26 | - |  |  | SI | Desea agregar Observaciones? (PAP) |
| Q27 | - |  |  | SI | Desea agregar Observaciones? (Mamografia) |
| Q28 | - |  |  | SI | Orgasmo |
| Q29 | - |  |  | SI | Frecuencia |
| Q30 | - |  |  | SI | Actividad Sexual-Líbido |
| Q31 | - |  |  | SI | Antecedente de Incontinencia Urinaria |
| Q32 | - |  |  | SI | Alteración Intervalo/Duración |
| Q33 | - |  |  | SI | Alteración de la cantidad |
| Q34 | - |  |  | SI | Otras Alteraciones |
| Q35 | - |  |  | SI | Alteraciones del Coito |
| Q36 | - |  |  | SI | Método Anticonceptivo |
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
| STF_Childsub | double |  |  | NO | Childsub |
| STF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STF_CreatedDate | date |  |  | SI | Created Date |
| STF_CreatedTime | time |  |  | SI | Created Time |
| STF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STF_GenericRouteForm_DR | varchar |  | FK | SI | Des Ref GenericRouteForm |
| STF_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| STF_INCI_DR | bigint |  | FK | SI | Des Ref INCI |
| STF_Max | double |  |  | SI | Max |
| STF_Min | double |  |  | SI | Min |
| STF_Position | varchar |  |  | SI | Position |
| STF_RowId | varchar |  |  | NO | - |
| STF_Sequence | double |  |  | SI | Sequence |
| STF_UpdatedDate | date |  |  | SI | Updated Date |
| STF_UpdatedTime | time |  |  | SI | Updated Time |
| STF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*