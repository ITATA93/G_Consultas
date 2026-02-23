# SQLUser.ORC_AirwayTechnique

**Schema:** SQLUser
**Columnas:** 198
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AIRTEC_RowId | bigint | PK |  | NO | - |
| AIRTEC_Code | varchar |  |  | NO | Code |
| AIRTEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AIRTEC_CreatedDate | date |  |  | SI | Created Date |
| AIRTEC_CreatedTime | time |  |  | SI | Created Time |
| AIRTEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AIRTEC_DateFrom | date |  |  | SI | Date From |
| AIRTEC_DateTo | date |  |  | SI | Date To |
| AIRTEC_Desc | varchar |  |  | NO | Description |
| AIRTEC_Owner | varchar |  |  | SI | Owner |
| AIRTEC_UpdatedDate | date |  |  | SI | Updated Date |
| AIRTEC_UpdatedTime | time |  |  | SI | Updated Time |
| AIRTEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Spinal Alignment |
| Q02 | - |  |  | SI | Cervical spine in sagittal plane (sitting) |
| Q03 | - |  |  | SI | Cervical spine in sagittal plane (sitting) Limitat... |
| Q04 | - |  |  | SI | Cervical spine in sagittal plane (sitting) Score |
| Q05 | - |  |  | SI | Thoracic spine in sagittal plane (sitting) |
| Q06 | - |  |  | SI | Thoracic spine in sagittal plane Limitation |
| Q07 | - |  |  | SI | Thoracic spine in sagittal plane Score |
| Q08 | - |  |  | SI | Lumbar spine in sagittal plane (sitting) |
| Q09 | - |  |  | SI | Lumbar spine in sagittal plane (sitting) Limitatio... |
| Q10 | - |  |  | SI | Lumbar spine in sagittal plane (sitting) Score |
| Q100 | - |  |  | SI | Spinal Alignment Score |
| Q101 | - |  |  | SI | Joint and Movement |
| Q102 | - |  |  | SI | Joint and Movement |
| Q103 | - |  |  | SI | Joint and Movement |
| Q104 | - |  |  | SI | Joint and Movement |
| Q105 | - |  |  | SI | Joint and Movement |
| Q106 | - |  |  | SI | Joint and Movement |
| Q107 | - |  |  | SI | Joint and Movement |
| Q108 | - |  |  | SI | Joint and Movement |
| Q109 | - |  |  | SI | Joint and Movement |
| Q11 | - |  |  | SI | Spinal alignment in frontal and transverse plane (... |
| Q110 | - |  |  | SI | Joint and Movement |
| Q111 | - |  |  | SI | Joint and Movement |
| Q112 | - |  |  | SI | Limitation |
| Q113 | - |  |  | SI | Limitation |
| Q114 | - |  |  | SI | Limitation |
| Q115 | - |  |  | SI | Limitation |
| Q116 | - |  |  | SI | Limitation |
| Q117 | - |  |  | SI | Limitation |
| Q118 | - |  |  | SI | Limitation |
| Q119 | - |  |  | SI | Limitation |
| Q12 | - |  |  | SI | Spinal alignment in frontal and transverse plane (... |
| Q120 | - |  |  | SI | Limitation |
| Q121 | - |  |  | SI | Limitation |
| Q122 | - |  |  | SI | Limitation |
| Q123 | - |  |  | SI | Right |
| Q124 | - |  |  | SI | Right |
| Q125 | - |  |  | SI | Right |
| Q126 | - |  |  | SI | Right |
| Q127 | - |  |  | SI | Right |
| Q128 | - |  |  | SI | Right |
| Q129 | - |  |  | SI | Right |
| Q13 | - |  |  | SI | Spinal alignment in frontal and transverse plane (... |
| Q130 | - |  |  | SI | Right |
| Q131 | - |  |  | SI | Right |
| Q132 | - |  |  | SI | Right |
| Q133 | - |  |  | SI | Right |
| Q134 | - |  |  | SI | Left |
| Q135 | - |  |  | SI | Left |
| Q136 | - |  |  | SI | Left |
| Q137 | - |  |  | SI | Left |
| Q138 | - |  |  | SI | Left |
| Q139 | - |  |  | SI | Left |
| Q14 | - |  |  | SI | Total of Spinal Alignment Score |
| Q140 | - |  |  | SI | Left |
| Q141 | - |  |  | SI | Left |
| Q142 | - |  |  | SI | Left |
| Q143 | - |  |  | SI | Left |
| Q144 | - |  |  | SI | Left |
| Q145 | - |  |  | SI | test |
| Q15 | - |  |  | SI | Mean Value (Total of Spinal Alignment) |
| Q16 | - |  |  | SI | Range Of Motion And Muscle Extensibility |
| Q17 | - |  |  | SI | Hip Extension |
| Q18 | - |  |  | SI | Hip Extension Limitation |
| Q19 | - |  |  | SI | Hip Extension Right |
| Q20 | - |  |  | SI | Hip Extension Left |
| Q21 | - |  |  | SI | Hip Flexion |
| Q22 | - |  |  | SI | Hip Flexion Limitation |
| Q23 | - |  |  | SI | Hip Flexion Right |
| Q24 | - |  |  | SI | Hip Flexion Left |
| Q25 | - |  |  | SI | Hip Abduction |
| Q26 | - |  |  | SI | Hip Abduction Limitation |
| Q27 | - |  |  | SI | Hip Abduction Right |
| Q28 | - |  |  | SI | Hip Abduction Left |
| Q29 | - |  |  | SI | Hip Adduction |
| Q30 | - |  |  | SI | Hip Adduction Limitation |
| Q31 | - |  |  | SI | Hip Adduction Right |
| Q32 | - |  |  | SI | Hip Adduction Left |
| Q33 | - |  |  | SI | Hip External Rotation |
| Q34 | - |  |  | SI | Hip External Rotation Limitation |
| Q35 | - |  |  | SI | Hip External Rotation Right |
| Q36 | - |  |  | SI | Hip External Rotation Left |
| Q37 | - |  |  | SI | Hip Internal Rotation |
| Q38 | - |  |  | SI | Hip Internal Rotation Limitation |
| Q39 | - |  |  | SI | Hip Internal Rotation Right |
| Q40 | - |  |  | SI | Hip Internal Rotation Left |
| Q41 | - |  |  | SI | Total Hip Score |
| Q42 | - |  |  | SI | Mean Value (Total Hip Score) |
| Q43 | - |  |  | SI | Knee Flexion |
| Q44 | - |  |  | SI | Knee Flexion Limitation |
| Q45 | - |  |  | SI | Knee Flexion Right |
| Q46 | - |  |  | SI | Knee Flexion Left |
| Q47 | - |  |  | SI | Hamstrings |
| Q48 | - |  |  | SI | Hamstrings Limitation |
| Q49 | - |  |  | SI | Hamstrings Right |
| Q50 | - |  |  | SI | Hamstrings left |
| Q51 | - |  |  | SI | Total Knee Score |
| Q52 | - |  |  | SI | Mean Value (Total Knee Score) |
| Q53 | - |  |  | SI | Ankle Dorsiflexion |
| Q54 | - |  |  | SI | Ankle Dorsiflexion Limitation |
| Q55 | - |  |  | SI | Ankle Dorsiflexion Right |
| Q56 | - |  |  | SI | Ankle Dorsiflexion Left |
| Q57 | - |  |  | SI | Ankle Plantarflexion |
| Q58 | - |  |  | SI | Ankle Plantarflexion Limitation |
| Q59 | - |  |  | SI | Ankle Plantarflexion Right |
| Q60 | - |  |  | SI | Ankle Plantarflexion Left |
| Q61 | - |  |  | SI | Total Ankle Score |
| Q62 | - |  |  | SI | Mean Value (Total Ankle Score) |
| Q63 | - |  |  | SI | Upper Extremities |
| Q64 | - |  |  | SI | Upper Extremities Limitations |
| Q65 | - |  |  | SI | Upper Extremities Right |
| Q66 | - |  |  | SI | Upper Extremities Left |
| Q67 | - |  |  | SI | Total Upper Extremities Score |
| Q68 | - |  |  | SI | Mean Value (Total Upper Extremities Score) |
| Q69 | - |  |  | SI | Range of Motion Score |
| Q70 | - |  |  | SI | Total SAROMM Score |
| Q71 | - |  |  | SI | Comments |
| Q72 | - |  |  | SI | Please note any other areas of joint management or... |
| Q73 | - |  |  | SI | Note |
| Q74 | - |  |  | SI | Variations to testing protocol or positions here |
| Q75 | - |  |  | SI | Total Score of (hip+knee+ankle+UE) |
| Q76 | - |  |  | SI | Total Score of (spinal alignment+range of motion) |
| Q77 | - |  |  | SI | Spine and Plane |
| Q78 | - |  |  | SI | Limitation |
| Q79 | - |  |  | SI | Spinal Aligment Score |
| Q80 | - |  |  | SI | Joint and Movement |
| Q81 | - |  |  | SI | Limitation |
| Q82 | - |  |  | SI | Right |
| Q83 | - |  |  | SI | Left |
| Q84 | - |  |  | SI | joint malalignment or limitations |
| Q85 | - |  |  | SI | in the range of motion |
| Q86 | - |  |  | SI | or positions here |
| Q87 | - |  |  | SI | Date |
| Q88 | - |  |  | SI | Time |
| Q89 | - |  |  | SI | Spine and Plane |
| Q90 | - |  |  | SI | Spine and Plane |
| Q91 | - |  |  | SI | Limitation |
| Q92 | - |  |  | SI | Limitation |
| Q93 | - |  |  | SI | Spinal Alignment Score |
| Q94 | - |  |  | SI | Spinal Alignment Score |
| Q95 | - |  |  | SI | Spine and Plane |
| Q96 | - |  |  | SI | Spine and Plane |
| Q97 | - |  |  | SI | Limitation |
| Q98 | - |  |  | SI | Limitation |
| Q99 | - |  |  | SI | Spinal Alignment Score |
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