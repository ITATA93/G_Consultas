# SQLUser.MRC_ObservationStatus

**Schema:** SQLUser
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBSST_RowId | bigint | PK |  | NO | - |
| OBSST_AlternativeCode | varchar |  |  | SI | Alternative Code |
| OBSST_Code | varchar |  |  | NO | Code |
| OBSST_CreatedDate | date |  |  | SI | Created Date |
| OBSST_CreatedTime | time |  |  | SI | Created Time |
| OBSST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OBSST_Desc | varchar |  |  | NO | Description |
| OBSST_UpdatedDate | date |  |  | SI | Updated Date |
| OBSST_UpdatedTime | time |  |  | SI | Updated Time |
| OBSST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Roberto (Rosita) no juega con los otros niños, ¿Po... |
| Q02 | - |  |  | SI | A veces Roberto se despierta en medio de la noche,... |
| Q03 | - |  |  | SI | Roberto tuvo un sueño anoche, ¿Què soñò? |
| Q04 | - |  |  | SI | Roberto trajo ayer la libreta de notas, ¿Què pasò? |
| Q05 | - |  |  | SI | Roberto hizo rabiar a su mamà el otro dìa, ¿Por qu... |
| Q06 | - |  |  | SI | Roberto siente que lo tratan mal a veces, ¿Por què... |
| Q07 | - |  |  | SI | Roberto llegò a su casa llorando el otro dìa, ¿Què... |
| Q08 | - |  |  | SI | La mamà de Roberto esta muy enojada por algo, ¿Por... |
| Q09 | - |  |  | SI | Ayer pasò algo malo, ¿Por què? |
| Q10 | - |  |  | SI | Roberto no quiere ir a la escuela , ¿Por què? |
| Q11 | - |  |  | SI | Hay algo de su profesor que a Roberto le gusta muc... |
| Q12 | - |  |  | SI | A veces Roberto se enoja en la escuela, ¿Por què? |
| Q13 | - |  |  | SI | Roberto tiene miedo de algo,¿De què tiene miedo? |
| Q14 | - |  |  | SI | Roberto se fue de su casa, ¿Por què? |
| Q15 | - |  |  | SI | Cuando el papà de Roberto llega tarde en la noche,... |
| Q16 | - |  |  | SI | A veces Roberto no quiere hacer lo que su mamà le ... |
| Q17 | - |  |  | SI | El profesor de Roberto quiso hablar con  èl despuè... |
| Q18 | - |  |  | SI | Hay algo que a Roberto no le gusta de su papà, ¿Qu... |
| Q19 | - |  |  | SI | Roberto piensa que su papà y su mamà no lo quieren... |
| Q20 | - |  |  | SI | Roberto desearìa ser grande,  ¿Por què? |
| Q21 | - |  |  | SI | A veces Roberto pelea con sus hermanos, ¿Por què? |
| Q22 | - |  |  | SI | A Roberto no le gusta un niño de su clase, ¿Por qu... |
| Q23 | - |  |  | SI | A veces Roberto se pone nervioso en la escuela, ¿P... |
| Q24 | - |  |  | SI | A Roberto no le gusta que lo llamen a interrogacio... |
| Q25 | - |  |  | SI | Un dìa Roberto  y su mamà tuvieron una gran pelea,... |
| Q26 | - |  |  | SI | A Roberto le desagrada algo de profesor, ¿Què es? |
| Q27 | - |  |  | SI | A veces Roberto se pone muy triste, ¿Por què? |
| Q28 | - |  |  | SI | Roberto casi siempre quiere estar solo, ¿Por què? |
| Q29 | - |  |  | SI | Un dìa Roberto quiso correr lejos de la casa y que... |
| Q30 | - |  |  | SI | Si Roberto pudiera hacer lo que quisiera, ¿Què cre... |
| Q31 | - |  |  | SI | ¿Cuàntos años crees tu que tiene Roberto? |
| Q32 | - |  |  | SI | ¿Què es lo que Roberto desea màs en el mundo? |
| Q33 | - |  |  | SI | Si Roberto tuviera poderes màgicos y pudiera cambi... |
| Q34 | - |  |  | SI | SI Roberto pudiera convertirse en un animal, ¿Què ... |
| Q35 | - |  |  | SI | ¿Y què animal no serìa? , ¿Por què? |
| QR36 | - |  |  | SI | Si Roberto/Rosita volviera a nacer otra vez ¿qué l... |
| QR37 | - |  |  | SI | Evaluación Profesional (P01) |
| QR38 | - |  |  | SI | Evaluación Profesional (P02) |
| QR39 | - |  |  | SI | Evaluación Profesional (P03) |
| QR40 | - |  |  | SI | Evaluación Profesional (P04) |
| QR41 | - |  |  | SI | Evaluación Profesional (P05) |
| QR42 | - |  |  | SI | Evaluación Profesional (P06) |
| QR43 | - |  |  | SI | Evaluación Profesional (P07) |
| QR44 | - |  |  | SI | Evaluación Profesional (P08) |
| QR45 | - |  |  | SI | Evaluación Profesional (P09) |
| QR46 | - |  |  | SI | Evaluación Profesional (P10) |
| QR47 | - |  |  | SI | Evaluación Profesional (P11) |
| QR48 | - |  |  | SI | Evaluación Profesional (P12) |
| QR49 | - |  |  | SI | Evaluación Profesional (P13) |
| QR50 | - |  |  | SI | Evaluación Profesional (P14) |
| QR51 | - |  |  | SI | Evaluación Profesional (P15) |
| QR52 | - |  |  | SI | Evaluación Profesional (P16) |
| QR53 | - |  |  | SI | Evaluación Profesional (P17) |
| QR54 | - |  |  | SI | Evaluación Profesional (P18) |
| QR55 | - |  |  | SI | Evaluación Profesional (P19) |
| QR56 | - |  |  | SI | Evaluación Profesional (P20) |
| QR57 | - |  |  | SI | Evaluación Profesional (P21) |
| QR58 | - |  |  | SI | Evaluación Profesional (P22) |
| QR59 | - |  |  | SI | Evaluación Profesional (P23) |
| QR60 | - |  |  | SI | Evaluación Profesional (P24) |
| QR61 | - |  |  | SI | Evaluación Profesional (P25) |
| QR62 | - |  |  | SI | Evaluación Profesional (P26) |
| QR63 | - |  |  | SI | Evaluación Profesional (P27) |
| QR64 | - |  |  | SI | Evaluación Profesional (P28) |
| QR65 | - |  |  | SI | Evaluación Profesional (P29) |
| QR66 | - |  |  | SI | Evaluación Profesional (P30) |
| QR67 | - |  |  | SI | Evaluación Profesional (P31) |
| QR68 | - |  |  | SI | Evaluación Profesional (P32) |
| QR69 | - |  |  | SI | Evaluación Profesional (P33) |
| QR70 | - |  |  | SI | Evaluación Profesional (P34) |
| QR71 | - |  |  | SI | Evaluación Profesional (P35) |
| QR73 | - |  |  | SI | Roberto se fue a su pieza ¿por qué? |
| QRFam | - |  |  | SI | Resultado Ámbito Familiar |
| QResc | - |  |  | SI | Resultado Ámbito Escolar-Social |
| QRper | - |  |  | SI | Resultado Ámbito Personal |
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