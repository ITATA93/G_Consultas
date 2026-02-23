# SQLUser.LBC_BPRulePatient

**Schema:** SQLUser
**Columnas:** 232
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPRP_RowID | bigint | PK |  | NO | - |
| LBCBPRP_AdditionalBloodGroup_DR | bigint |  | FK | SI | Additional Blood Group |
| LBCBPRP_Antibody_DR | bigint |  | FK | SI | Antibody |
| LBCBPRP_BloodGroupStatus | varchar |  |  | SI | Blood Group Status |
| LBCBPRP_BloodGroup_DR | bigint |  | FK | SI | Blood Group |
| LBCBPRP_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCBPRP_CreatedDate | date |  |  | SI | Created Date |
| LBCBPRP_CreatedTime | time |  |  | SI | Created Time |
| LBCBPRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCBPRP_DateFrom | date |  |  | SI | Effective date for the record |
| LBCBPRP_DateTo | date |  |  | SI | Last day the record is active |
| LBCBPRP_Desc | varchar |  |  | SI | Rule Description |
| LBCBPRP_Desc_Calc | varchar |  |  | SI | Rule Calculated Description |
| LBCBPRP_Ethnicity_DR | bigint |  | FK | SI | Ethnicity |
| LBCBPRP_FullDesc | longvarchar |  |  | SI | Full Description
HTMLRichText |
| LBCBPRP_NotAdditionalBloodGroup | varchar |  |  | SI | Not Additional Blood Group
Logically negate the s... |
| LBCBPRP_Owner | varchar |  |  | SI | Owner |
| LBCBPRP_PatientFlag_DR | bigint |  | FK | SI | Patient Flag |
| LBCBPRP_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCBPRP_Sex_DR | bigint |  | FK | SI | Sex |
| LBCBPRP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCBPRP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCBPRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Servicio |
| Q02 | - |  |  | SI | Régimen |
| Q03 | - |  |  | SI | Fecha |
| Q04 | - |  |  | SI | Cama |
| Q05 | - |  |  | SI | Sala |
| QE01 | - |  |  | SI | Entrega GRS 01 |
| QE02 | - |  |  | SI | Entrega GRS 02 |
| QE03 | - |  |  | SI | Entrega GRS 03 |
| QE04 | - |  |  | SI | Entrega GRS 04 |
| QE05 | - |  |  | SI | Entrega GRS 05 |
| QE06 | - |  |  | SI | Entrega GRS 06 |
| QE07 | - |  |  | SI | Entrega GRS 07 |
| QE08 | - |  |  | SI | Entrega GRS 08 |
| QE09 | - |  |  | SI | Entrega GRS 09 |
| QE10 | - |  |  | SI | Entrega GRS 10 |
| QE11 | - |  |  | SI | Entrega GRS 11 |
| QE12 | - |  |  | SI | Entrega GRS 12 |
| QE13 | - |  |  | SI | Entrega GRS 13 |
| QE14 | - |  |  | SI | Entrega GRS 14 |
| QE15 | - |  |  | SI | Entrega GRS 15 |
| QE16 | - |  |  | SI | Entrega GRS 16 |
| QE17 | - |  |  | SI | Entrega GRS 17 |
| QE18 | - |  |  | SI | Entrega GRS 18 |
| QE19 | - |  |  | SI | Entrega GRS 19 |
| QE20 | - |  |  | SI | Entrega GRS 20 |
| QEC01 | - |  |  | SI | Entrega CC 01 |
| QEC02 | - |  |  | SI | Entrega CC 02 |
| QEC03 | - |  |  | SI | Entrega CC 03 |
| QEC04 | - |  |  | SI | Entrega CC 04 |
| QEC05 | - |  |  | SI | Entrega CC 05 |
| QEC06 | - |  |  | SI | Entrega CC 06 |
| QEC07 | - |  |  | SI | Entrega CC 07 |
| QEC08 | - |  |  | SI | Entrega CC 08 |
| QEC09 | - |  |  | SI | Entrega CC 09 |
| QEC10 | - |  |  | SI | Entrega CC 10 |
| QEC11 | - |  |  | SI | Entrega CC 11 |
| QEC12 | - |  |  | SI | Entrega CC 12 |
| QEC13 | - |  |  | SI | Entrega CC 13 |
| QEC14 | - |  |  | SI | Entrega CC 14 |
| QEC15 | - |  |  | SI | Entrega CC 15 |
| QEC16 | - |  |  | SI | Entrega CC 16 |
| QEC17 | - |  |  | SI | Entrega CC 17 |
| QEC18 | - |  |  | SI | Entrega CC 18 |
| QEC19 | - |  |  | SI | Entrega CC 19 |
| QEC20 | - |  |  | SI | Entrega CC 20 |
| QH01 | - |  |  | SI | Hora 01 |
| QH02 | - |  |  | SI | Hora 02 |
| QH03 | - |  |  | SI | Hora 03 |
| QH04 | - |  |  | SI | Hora 04 |
| QH05 | - |  |  | SI | Hora 05 |
| QH06 | - |  |  | SI | Hora 06 |
| QH07 | - |  |  | SI | Hora 07 |
| QH08 | - |  |  | SI | Hora 08 |
| QH09 | - |  |  | SI | Hora 09 |
| QH10 | - |  |  | SI | Hora 10 |
| QH11 | - |  |  | SI | Hora 11 |
| QH12 | - |  |  | SI | Hora 12 |
| QH13 | - |  |  | SI | Hora 13 |
| QH14 | - |  |  | SI | Hora 14 |
| QH15 | - |  |  | SI | Hora 15 |
| QH16 | - |  |  | SI | Hora 16 |
| QH17 | - |  |  | SI | Hora 17 |
| QH18 | - |  |  | SI | Hora 18 |
| QH19 | - |  |  | SI | Hora 19 |
| QH20 | - |  |  | SI | Hora 20 |
| QI01 | - |  |  | SI | Ingreso GRS 01 |
| QI02 | - |  |  | SI | Ingreso GRS 02 |
| QI03 | - |  |  | SI | Ingreso GRS 03 |
| QI04 | - |  |  | SI | Ingreso GRS 04 |
| QI05 | - |  |  | SI | Ingreso GRS 05 |
| QI06 | - |  |  | SI | Ingreso GRS 06 |
| QI07 | - |  |  | SI | Ingreso GRS 07 |
| QI08 | - |  |  | SI | Ingreso GRS 08 |
| QI09 | - |  |  | SI | Ingreso GRS 09 |
| QI10 | - |  |  | SI | Ingreso GRS 10 |
| QI11 | - |  |  | SI | Ingreso GRS 11 |
| QI12 | - |  |  | SI | Ingreso GRS 12 |
| QI13 | - |  |  | SI | Ingreso GRS 13 |
| QI14 | - |  |  | SI | Ingreso GRS 14 |
| QI15 | - |  |  | SI | Ingreso GRS 15 |
| QI16 | - |  |  | SI | Ingreso GRS 16 |
| QI17 | - |  |  | SI | Ingreso GRS 17 |
| QI18 | - |  |  | SI | Ingreso GRS 18 |
| QI19 | - |  |  | SI | Ingreso GRS 19 |
| QI20 | - |  |  | SI | Ingreso GRS 20 |
| QIC01 | - |  |  | SI | Ingreso CC 01 |
| QIC02 | - |  |  | SI | Ingreso CC 02 |
| QIC03 | - |  |  | SI | Ingreso CC 03 |
| QIC04 | - |  |  | SI | Ingreso CC 04 |
| QIC05 | - |  |  | SI | Ingreso CC 05 |
| QIC06 | - |  |  | SI | Ingreso CC 06 |
| QIC07 | - |  |  | SI | Ingreso CC 07 |
| QIC08 | - |  |  | SI | Ingreso CC 08 |
| QIC09 | - |  |  | SI | Ingreso CC 09 |
| QIC10 | - |  |  | SI | Ingreso CC 10 |
| QIC11 | - |  |  | SI | Ingreso CC 11 |
| QIC12 | - |  |  | SI | Ingreso CC 12 |
| QIC13 | - |  |  | SI | Ingreso CC 13 |
| QIC14 | - |  |  | SI | Ingreso CC 14 |
| QIC15 | - |  |  | SI | Ingreso CC 15 |
| QIC16 | - |  |  | SI | Ingreso CC 16 |
| QIC17 | - |  |  | SI | Ingreso CC 17 |
| QIC18 | - |  |  | SI | Ingreso CC 18 |
| QIC19 | - |  |  | SI | Ingreso CC 19 |
| QIC20 | - |  |  | SI | Ingreso CC 20 |
| QP01 | - |  |  | SI | Preparación 01 |
| QP02 | - |  |  | SI | Preparación 02 |
| QP03 | - |  |  | SI | Preparación 03 |
| QP04 | - |  |  | SI | Preparación 04 |
| QP05 | - |  |  | SI | Preparación 05 |
| QP06 | - |  |  | SI | Preparación 06 |
| QP07 | - |  |  | SI | Preparación 07 |
| QP08 | - |  |  | SI | Preparación 08 |
| QP09 | - |  |  | SI | Preparación 09 |
| QP10 | - |  |  | SI | Preparación 10 |
| QP11 | - |  |  | SI | Preparación 11 |
| QP12 | - |  |  | SI | Preparación 12 |
| QP13 | - |  |  | SI | Preparación 13 |
| QP14 | - |  |  | SI | Preparación 14 |
| QP15 | - |  |  | SI | Preparación 15 |
| QP16 | - |  |  | SI | Preparación 16 |
| QP17 | - |  |  | SI | Preparación 17 |
| QP18 | - |  |  | SI | Preparación 18 |
| QP19 | - |  |  | SI | Preparación 19 |
| QP20 | - |  |  | SI | Preparación 20 |
| QR01 | - |  |  | SI | Restante 01 |
| QR02 | - |  |  | SI | Restante 02 |
| QR03 | - |  |  | SI | Restante 03 |
| QR04 | - |  |  | SI | Restante 04 |
| QR05 | - |  |  | SI | Restante 05 |
| QR06 | - |  |  | SI | Restante 06 |
| QR07 | - |  |  | SI | Restante 07 |
| QR08 | - |  |  | SI | Restante 08 |
| QR09 | - |  |  | SI | Restante 09 |
| QR10 | - |  |  | SI | Restante 10 |
| QR11 | - |  |  | SI | Restante 11 |
| QR12 | - |  |  | SI | Restante 12 |
| QR13 | - |  |  | SI | Restante 13 |
| QR14 | - |  |  | SI | Restante 14 |
| QR15 | - |  |  | SI | Restante 15 |
| QR16 | - |  |  | SI | Restante 16 |
| QR17 | - |  |  | SI | Restante 17 |
| QR18 | - |  |  | SI | Restante 18 |
| QR19 | - |  |  | SI | Restante 19 |
| QR20 | - |  |  | SI | Restante 20 |
| QRC01 | - |  |  | SI | Restante CC 01 |
| QRC02 | - |  |  | SI | Restante CC 02 |
| QRC03 | - |  |  | SI | Restante CC 03 |
| QRC04 | - |  |  | SI | Restante CC 04 |
| QRC05 | - |  |  | SI | Restante CC 05 |
| QRC06 | - |  |  | SI | Restante CC 06 |
| QRC07 | - |  |  | SI | Restante CC 07 |
| QRC08 | - |  |  | SI | Restante CC 08 |
| QRC09 | - |  |  | SI | Restante CC 09 |
| QRC10 | - |  |  | SI | Restante CC 10 |
| QRC11 | - |  |  | SI | Restante CC 11 |
| QRC12 | - |  |  | SI | Restante CC 12 |
| QRC13 | - |  |  | SI | Restante CC 13 |
| QRC14 | - |  |  | SI | Restante CC 14 |
| QRC15 | - |  |  | SI | Restante CC 15 |
| QRC16 | - |  |  | SI | Restante CC 16 |
| QRC17 | - |  |  | SI | Restante CC 17 |
| QRC18 | - |  |  | SI | Restante CC 18 |
| QRC19 | - |  |  | SI | Restante CC 19 |
| QRC20 | - |  |  | SI | Restante CC 20 |
| QTICC | - |  |  | SI | TOTAL INGESTA CC |
| QTIGRS | - |  |  | SI | TOTAL INGESTA GRS |
| QTRCC | - |  |  | SI | TOTAL RESTANTE CC |
| QTRGRS | - |  |  | SI | TOTAL RESTANTE GRS |
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