# SQLUser.ARC_DerivedFeeRules

**Schema:** SQLUser
**Columnas:** 139
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DFR_RowId | bigint | PK |  | NO | - |
| ChildQ30DR | - |  |  | SI | Child Reference: Orejas Alteradas |
| DFR_ARCIM1_DR | varchar |  | FK | SI | Des Ref ARCIM1 |
| DFR_ARCIM2_DR | varchar |  | FK | SI | Des Ref ARCIM2 |
| DFR_Amount1 | double |  |  | SI | Fixed Amount |
| DFR_Amount2 | double |  |  | SI | Fixed Amount |
| DFR_Amount3 | double |  |  | SI | Amount3 |
| DFR_Code | varchar |  |  | NO | Code |
| DFR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DFR_CreatedDate | date |  |  | SI | Created Date |
| DFR_CreatedTime | time |  |  | SI | Created Time |
| DFR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DFR_Desc | varchar |  |  | NO | Description |
| DFR_FeePerPatient | double |  |  | SI | Fee Per Patient |
| DFR_NumberOfPatients | double |  |  | SI | Number Of Patients |
| DFR_Owner | varchar |  |  | SI | Owner |
| DFR_UpdatedDate | date |  |  | SI | Updated Date |
| DFR_UpdatedTime | time |  |  | SI | Updated Time |
| DFR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Flexión esperada para la edad, con movimientos act... |
| Q02 | - |  |  | SI | Piel Alterada |
| Q03 | - |  |  | SI | Lanugo Alterado |
| Q04 | - |  |  | SI | Comentarios actitud general |
| Q10 | - |  |  | SI | Cráneo simétrico, sin deformidades ni cefalohemato... |
| Q101 | - |  |  | SI | Resto del examen realizado en caderas y columnas, ... |
| Q102 | - |  |  | SI | Resto del examen realizado en extremidades, sin al... |
| Q103 | - |  |  | SI | Resto del examen realizado en región anal, sin alt... |
| Q104 | - |  |  | SI | Resto del examen realizado en genitales femeninos,... |
| Q105 | - |  |  | SI | Resto del examen realizado en genitales masculinos... |
| Q106 | - |  |  | SI | Resto del examen realizado en ombligo y cordón, si... |
| Q107 | - |  |  | SI | Resto del examen realizado en Abdomen, sin alterac... |
| Q108 | - |  |  | SI | Resto del examen realizado en mamas, sin alteracio... |
| Q109 | - |  |  | SI | Resto del examen realizado en claviculas, sin alte... |
| Q11 | - |  |  | SI | Cráneo Alterado |
| Q12 | - |  |  | SI | Cráneo Alterado Comentarios |
| Q123 | - |  |  | SI | Profesional de Salud |
| Q14 | - |  |  | SI | Fascie no característica, sin asimetrías ni paráli... |
| Q15 | - |  |  | SI | Cara Comentarios |
| Q17 | - |  |  | SI | No presenta hemangiomas subconjuntivales. Pupilas ... |
| Q19 | - |  |  | SI | Pupilas Alteradas |
| Q20 | - |  |  | SI | Ojos Comentarios |
| Q200 | - |  |  | SI | Piel Descripción |
| Q201 | - |  |  | SI | Lanugo Descripción |
| Q202 | - |  |  | SI | Hemangiomas Descripción |
| Q204 | - |  |  | SI | Cardiaco Descripción |
| Q205 | - |  |  | SI | Extremidades Descripción |
| Q206 | - |  |  | SI | Reflejo Descripción |
| Q22 | - |  |  | SI | Nariz Alterada |
| Q23 | - |  |  | SI | Nariz Comentarios |
| Q24 | - |  |  | SI | Adecuada para la edad, sin estridor, ni atresia de... |
| Q26 | - |  |  | SI | Cavidad bucal adecuada para la edad, no presenta d... |
| Q27 | - |  |  | SI | Boca alterada |
| Q28 | - |  |  | SI | Boca Comentarios |
| Q31 | - |  |  | SI | Orejas Comentarios |
| Q32 | - |  |  | SI | Pabellones auriculares adecuados para la edad, no ... |
| Q34 | - |  |  | SI | Cuello Alterado |
| Q35 | - |  |  | SI | Cuello Comentario |
| Q36 | - |  |  | SI | Región cervical adecuada, no presenta tortícolis, ... |
| Q39 | - |  |  | SI | Pulmonar Comentarios |
| Q40 | - |  |  | SI | Adecuado para la edad, cilíndrico, blando, murmull... |
| Q43 | - |  |  | SI | Ritmo regular en dos tiempos, sin ruidos agregados... |
| Q45 | - |  |  | SI | Clavícula Alterada |
| Q46 | - |  |  | SI | Clavicula Comentarios |
| Q47 | - |  |  | SI | Clavículas simétricas, sin signos de lesión |
| Q49 | - |  |  | SI | Mamas Comentarios |
| Q50 | - |  |  | SI | Areola completa, glándula presente. |
| Q53 | - |  |  | SI | Abdomen Comentarios |
| Q54 | - |  |  | SI | Abdomen simétrico, depresible, ruidos hidroaéreos ... |
| Q56 | - |  |  | SI | Ombligo Alterado |
| Q57 | - |  |  | SI | Ombligo comentarios |
| Q58 | - |  |  | SI | Rosado, sin hernias, tres vasos. |
| Q59 | - |  |  | SI | Genitales Masculinos Comentarios |
| Q60 | - |  |  | SI | Genitales Masculinos alterados |
| Q61 | - |  |  | SI | Genitales masculinos adecuados para la edad, testí... |
| Q63 | - |  |  | SI | Genitales Femeninos Comentarios |
| Q64 | - |  |  | SI | Genitales femeninos adecuados para la edad, labios... |
| Q66 | - |  |  | SI | Ano anormal |
| Q67 | - |  |  | SI | Comentario ano |
| Q68 | - |  |  | SI | Ano con esfínter funcional, sin fístulas. |
| Q72 | - |  |  | SI | Adecuadas en cuanto al tamaño y forma, dedos bien ... |
| Q74 | - |  |  | SI | Extremidades Inferiores Alteradas |
| Q75 | - |  |  | SI | Extremidades Inferiores Comentarios |
| Q76 | - |  |  | SI | Caderas simétricas, columna en postura adecuada pa... |
| Q78 | - |  |  | SI | Columna Alterada |
| Q79 | - |  |  | SI | Columna comentarios |
| Q80 | - |  |  | SI | Columna en postura adecuada para la edad, sin defo... |
| Q87 | - |  |  | SI | Resto del examen cardiaco realizado, sin alteracio... |
| Q88 | - |  |  | SI | Resto del examen pulmonar realizado, sin alteracio... |
| Q89 | - |  |  | SI | Resto del examen realizado en cuello, sin alteraci... |
| Q90 | - |  |  | SI | Resto del examen realizado en orejas alteradas, si... |
| Q91 | - |  |  | SI | Resto del examen realizado en boca, sin alteracion... |
| Q92 | - |  |  | SI | Resto del examen realizado en nariz, sin alteracio... |
| Q93 | - |  |  | SI | Resto del examen realizado en pupilas, sin alterac... |
| Q94 | - |  |  | SI | Resto del examen realizado en cara, sin alteracion... |
| Q95 | - |  |  | SI | Resto del examen realizado en cráneo, sin alteraci... |
| Q96 | - |  |  | SI | Resto del examen realizado en hemangiomas y mancha... |
| Q97 | - |  |  | SI | Resto del examen realizado en lanugo, sin alteraci... |
| Q98 | - |  |  | SI | Resto del examen realizado en piel, sin alteracion... |
| Q99 | - |  |  | SI | Resto del examen realizado en actitud general, sin... |
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