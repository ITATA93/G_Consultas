# SQLUser.CT_CareProvORPrefEq

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Profesionales**. Médicos y personal de salud.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EQ_ParRef | varchar | PK |  | NO | CT_CareProvORPref Parent Reference |
| EQ_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| EQ_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| EQ_CTPCP_DR | varchar |  | FK | SI | Des Ref CTPCP |
| EQ_CareProvType | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017.2+ and re... |
| EQ_Childsub | double |  |  | NO | Childsub |
| EQ_CreatedDate | date |  |  | SI | Created Date |
| EQ_CreatedTime | time |  |  | SI | Created Time |
| EQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EQ_DateActiveFrom | date |  |  | SI | DateActiveFrom |
| EQ_DateActiveTo | date |  |  | SI | DateActiveTo |
| EQ_EquipQty | double |  |  | SI | EquipQty |
| EQ_Equip_DR | varchar |  | FK | SI | Des Ref ARCIM |
| EQ_ORCEquipDR | bigint |  | FK | SI | Des Ref EquipDR |
| EQ_OperatingStaffRole_DR | bigint |  | FK | SI | Des Ref ORC_OperatingStaffRole |
| EQ_PersonalHTMLPlainText | longvarbinary |  |  | SI | Personal Preference Text (HTMLPlainText) as Binary... |
| EQ_PersonalHTMLRichText | longvarbinary |  |  | SI | Personal Preference Text (HTMLRichText) as BinaryS... |
| EQ_PersonalImgAnnotation | longvarbinary |  |  | SI | Personal Preference Image Annotation as BinaryStre... |
| EQ_PersonalImgDoc | longvarbinary |  |  | SI | Personal Preference Image as BinaryStream |
| EQ_PersonalPrefType | varchar |  |  | SI | Personal Preference Type |
| EQ_Qty | double |  |  | SI | Qty |
| EQ_Remarks | varchar |  |  | SI | Remarks |
| EQ_RowId | varchar |  |  | NO | - |
| EQ_SequenceNo | varchar |  |  | SI | SequenceNo |
| EQ_StaffQty | double |  |  | SI | StaffQty |
| EQ_Text1 | varchar |  |  | SI | Text1 |
| EQ_UpdateDate | date |  |  | SI | UpdateDate |
| EQ_UpdateTime | time |  |  | SI | UpdateTime |
| EQ_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| EQ_UpdatedDate | date |  |  | SI | Updated Date |
| EQ_UpdatedTime | time |  |  | SI | Updated Time |
| EQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | Responsable |
| Q04 | - |  |  | SI | Consigna: Lea estas palabras en voz alta e intente... |
| Q05 | - |  |  | SI | Lectura 5 palabras |
| Q06 | - |  |  | SI | Total lectura 5 palabras |
| Q07 | - |  |  | SI | Consigna: Puede ahora, mirándo la hoja, decirme ¿c... |
| Q08 | - |  |  | SI | Identificación 5 palabras |
| Q09 | - |  |  | SI | Total identificación 5 palabras |
| Q10 | - |  |  | SI | Recuerdo libre inmediato 5 palabras |
| Q11 | - |  |  | SI | Total Recuerdo libre inmediato 5 palabras |
| Q12 | - |  |  | SI | Intrusiones recuerdo libre inmedito |
| Q13 | - |  |  | SI | Total Intrusiones recuerdo libre  inmedito |
| Q14 | - |  |  | SI | Consigna: ¿Cuál era la flor? |
| Q15 | - |  |  | SI | Recuerdo con Clave Inmediato |
| Q16 | - |  |  | SI | Intrusiones recuerdo con Clave Inmedito |
| Q17 | - |  |  | SI | Intrusiones Recuerdo con Clave  Inmedito |
| Q18 | - |  |  | SI | Total Recuerdo inmediato con clave |
| Q19 | - |  |  | SI | Total Intrusiones Recuerdo Inmediato |
| Q20 | - |  |  | SI | Número de ensayos necesarios para aprender las 5 p... |
| Q21 | - |  |  | SI | Consigna: Dígame todas las palabras que recuerde |
| Q22 | - |  |  | SI | Recuerdo diferido libre 5 palabras |
| Q23 | - |  |  | SI | Recuerdo diferido libre 5 palabras |
| Q24 | - |  |  | SI | Intrusiones recuerdo diferido libre |
| Q25 | - |  |  | SI | Intrusiones recuerdo diferido libre |
| Q26 | - |  |  | SI | Consigna: ¿Cuál era la flor? |
| Q27 | - |  |  | SI | Recuerdo diferido con clave 5 palabras |
| Q28 | - |  |  | SI | Intrusiones recuerdo diferido con clave |
| Q29 | - |  |  | SI | Intrusiones recuerdo diferido con clave |
| Q30 | - |  |  | SI | Total intrusiones recuerdo diferido |
| Q31 | - |  |  | SI | Total recuerdo diferido con clave 5 palabras |
| Q32 | - |  |  | SI | Puntaje total recuerdo inmediato |
| Q33 | - |  |  | SI | Puntaje total recuerdo diferido |
| Q34 | - |  |  | SI | Puntaje total 5 palabras |
| Q35 | - |  |  | SI | Puntaje total Intrusiones |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*