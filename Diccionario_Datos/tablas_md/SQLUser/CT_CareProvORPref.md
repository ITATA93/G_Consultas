# SQLUser.CT_CareProvORPref

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Profesionales**. Médicos y personal de salud.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORP_ParRef | varchar | PK |  | NO | CT_CareProv Parent Reference |
| ORP_AnaestMethod_DR | bigint |  | FK | SI | Des Ref AnaestMethod |
| ORP_AvAnaesTime | double |  |  | SI | Average Anaesthetic Time(minutes), Anaesthetic Tim... |
| ORP_AverageProcTime | double |  |  | SI | AverageProcTime |
| ORP_CalcAvgPrevDetails | varchar |  |  | SI | CalcAvgPrevDetails |
| ORP_Childsub | double |  |  | NO | Childsub |
| ORP_CreatedDate | date |  |  | SI | Created Date |
| ORP_CreatedTime | time |  |  | SI | Created Time |
| ORP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORP_DefaultAnaesMeth_DR | bigint |  | FK | SI | Default Anaesthesia Method |
| ORP_ExpectedLOS | double |  |  | SI | ExpectedLOS |
| ORP_Notes | varchar |  |  | SI | Notes  |
| ORP_OperProc_DR | varchar |  | FK | SI | List of Operation/Procedure |
| ORP_Operation_DR | bigint |  | FK | SI | Des Ref Operation |
| ORP_PersonalHTMLPlainText | longvarbinary |  |  | SI | Personal Preference Text (HTMLPlainText) as Binary... |
| ORP_PersonalHTMLRichText | longvarbinary |  |  | SI | Personal Preference Text (HTMLRichText) as BinaryS... |
| ORP_PersonalImgAnnotation | longvarbinary |  |  | SI | Personal Preference Image Annotation as BinaryStre... |
| ORP_PersonalImgDoc | longvarbinary |  |  | SI | Personal Preference Image as BinaryStream |
| ORP_PersonalPrefType | varchar |  |  | SI | Personal Preference Type |
| ORP_PersonalProsthReq | varchar |  |  | SI | Prosthetics Required |
| ORP_PrevCleanUpTime | double |  |  | SI | Clean up Time (minutes), needed after the previous... |
| ORP_ProcSetupTime | double |  |  | SI | Pre/Set Up Time (minutes), setup time needed for t... |
| ORP_RecovOperation_DR | bigint |  | FK | SI | Des Ref RecovOperation |
| ORP_RecovStatePPP_DR | bigint |  | FK | SI | Des Ref RecovStatePPP |
| ORP_RecovText | varchar |  |  | SI | RecovText |
| ORP_RowId | varchar |  |  | NO | - |
| ORP_StatePPP_DR | bigint |  | FK | SI | Des Ref StatePPP |
| ORP_StatePPPs_DR | varchar |  | FK | SI | List of State PPP's |
| ORP_Text1 | varchar |  |  | SI | Text1 |
| ORP_TurnaroundTime | double |  |  | SI | Turnaround Time |
| ORP_UpdatedDate | date |  |  | SI | Updated Date |
| ORP_UpdatedTime | time |  |  | SI | Updated Time |
| ORP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Lugar Inicio Síntomas |
| Q02 | - |  |  | SI | Hubo Llamdo a Ambulancia |
| Q03 | - |  |  | SI | Se contactó a hospital antes de la llegada del pac... |
| Q04 | - |  |  | SI | ¿Se activó código ACV? |
| Q05 | - |  |  | SI | Medio de transporte en que paciente llega al hospi... |
| Q06 | - |  |  | SI | Hora Inicio de Síntomas |
| Q07 | - |  |  | SI | Hora Ingreso Admisión |
| Q08 | - |  |  | SI | Hora Triage Enfermería |
| Q09 | - |  |  | SI | Valor triage enfermería |
| Q10 | - |  |  | SI | Hora en que se solicitan los exámenes de laborator... |
| Q11 | - |  |  | SI | Hora en que los exámenes de sangre llegan al labor... |
| Q12 | - |  |  | SI | Hora atención médico urgencias |
| Q13 | - |  |  | SI | Hora inicio contacto telefónico neurólogo |
| Q14 | - |  |  | SI | Médico Urgenciólogo que presenta al paciente |
| Q15 | - |  |  | SI | Hora Inicio Teleconsulta Tele- ACV |
| Q16 | - |  |  | SI | Hora TAC Cerebral |
| Q17 | - |  |  | SI | Hora de Visualización TAC por Tele ACV |
| Q18 | - |  |  | SI | Diagnóstico de la Teleconsulta |
| Q19 | - |  |  | SI | Hora de la Decisión Terapéutica |
| Q20 | - |  |  | SI | Hora Inicio Trombolisis |
| Q201 | - |  |  | SI | No Aplica |
| Q21 | - |  |  | SI | ¿Se logra el tiempo puerta aguja menor a 60 minuto... |
| Q22 | - |  |  | SI | NIHSS Ingreso |
| Q23 | - |  |  | SI | NIHSS al Final de Trombolisis |
| Q24 | - |  |  | SI | NIHSS 24 Horas Post Trombolisis |
| Q25 | - |  |  | SI | RANKIN Estimado de Ingreso |
| Q26 | - |  |  | SI | RANKIN Estimado de Alta |
| Q28 | - |  |  | SI | NIHSS Ingreso Valor |
| Q29 | - |  |  | SI | NIHSS al Final de Trombolisis Valor |
| Q30 | - |  |  | SI | NIHSS 24 Horas Post Trombolisis Valor |
| Q31 | - |  |  | SI | Comentarios |
| Q32 | - |  |  | SI | Hora de resultado de examenes de laboratorio |
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