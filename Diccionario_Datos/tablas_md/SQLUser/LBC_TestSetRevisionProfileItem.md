# SQLUser.LBC_TestSetRevisionProfileItem

**Schema:** SQLUser
**Columnas:** 203
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRPRI_ParRef | varchar | PK |  | NO | Parent Revision Profile |
| ChildQ18DR | - |  |  | SI | Child Reference: no usado |
| LBCTSRPRI_Active | varchar |  |  | SI | - |
| LBCTSRPRI_Reportable | varchar |  |  | SI | - |
| LBCTSRPRI_Required | varchar |  |  | SI | - |
| LBCTSRPRI_RowID | varchar |  |  | NO | - |
| LBCTSRPRI_TestSetRevisionItem_DR | varchar |  | FK | SI | Test Set Revision Item |
| Q01 | - |  |  | SI | Flexión esperada para la edad, con movimientos act... |
| Q02 | - |  |  | SI | Piel |
| Q03 | - |  |  | SI | Lanugo |
| Q04 | - |  |  | SI | Comentarios actitud general |
| Q06 | - |  |  | SI | Comentario Hemangiomas |
| Q07 | - |  |  | SI | Mancha Mongólica |
| Q08 | - |  |  | SI | Descripción Mancha Mongólica |
| Q10 | - |  |  | SI | Cráneo simétrico, sin deformidades ni cefalohemato... |
| Q100 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q101 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q102 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q103 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q104 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q105 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q106 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q107 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q108 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q109 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q11 | - |  |  | SI | Cráneo Alterado |
| Q110 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q111 | - |  |  | SI | Fecha de Ingreso |
| Q112 | - |  |  | SI | Hora de Ingreso |
| Q114 | - |  |  | SI | Información entregada por |
| Q115 | - |  |  | SI | Contacto |
| Q116 | - |  |  | SI | Procedencia del paciente |
| Q117 | - |  |  | SI | Procedencia, descripción |
| Q12 | - |  |  | SI | Cráneo Alterado Comentarios |
| Q120 | - |  |  | SI | Anamnésis Próxima |
| Q121 | - |  |  | SI | Conclusiones |
| Q122 | - |  |  | SI | Plan de Manejo al Ingreso |
| Q123 | - |  |  | SI | Profesional de Salud |
| Q124 | - |  |  | SI | Fono Contacto |
| Q125 | - |  |  | SI | Fecha Nacimiento |
| Q126 | - |  |  | SI | Hora de Nacimiento |
| Q129 | - |  |  | SI | Sexo |
| Q130 | - |  |  | SI | Peso al Nacer |
| Q130ObsDR | - |  |  | SI | Peso al Nacer DR |
| Q131 | - |  |  | SI | Talla al Nacer |
| Q131ObsDR | - |  |  | SI | Talla al Nacer DR |
| Q132 | - |  |  | SI | Circunferencia Craneana |
| Q132ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q134 | - |  |  | SI | Apego |
| Q135 | - |  |  | SI | Apego Duración |
| Q14 | - |  |  | SI | Fascie no característica, sin asimetrías ni paráli... |
| Q141 | - |  |  | SI | Diuresis |
| Q143 | - |  |  | SI | Deposiciones |
| Q144 | - |  |  | SI | Lactancia Materna |
| Q145 | - |  |  | SI | Alimentación Complementaria |
| Q146 | - |  |  | SI | Administración Vitamina  K |
| Q147 | - |  |  | SI | Alimentación Complementaria |
| Q148 | - |  |  | SI | Reanimación |
| Q149 | - |  |  | SI | Profilaxis Ocular |
| Q15 | - |  |  | SI | Cara Comentarios |
| Q150 | - |  |  | SI | Anomalía Congénita |
| Q152 | - |  |  | SI | Muestra de Sangre de Cordón Grupo RH Coomb |
| Q153 | - |  |  | SI | Semanas de Gestación 1 |
| Q154 | - |  |  | SI | Semanas de Gestación 2 |
| Q155 | - |  |  | SI | Morbilidad RN |
| Q156 | - |  |  | SI | Apgar 1 Minuto |
| Q157 | - |  |  | SI | Apgar 5 Minutos |
| Q158 | - |  |  | SI | Apgar 10 Minutos |
| Q159 | - |  |  | SI | Nombre de la Madre |
| Q160 | - |  |  | SI | Edad Materna |
| Q161 | - |  |  | SI | Gesta |
| Q162 | - |  |  | SI | Número de Partos |
| Q163 | - |  |  | SI | Hijos Vivos |
| Q164 | - |  |  | SI | Grupo Sanguíneo Materno |
| Q165 | - |  |  | SI | Factor RH Materno |
| Q17 | - |  |  | SI | No presenta hemangiomas subconjuntivales. Pupilas ... |
| Q170 | - |  |  | SI | Patología del Embarazo |
| Q171 | - |  |  | SI | Medicamentos que tomó durante el embarazo |
| Q172 | - |  |  | SI | Tipo de Parto |
| Q173 | - |  |  | SI | Causa de Cesárea |
| Q174 | - |  |  | SI | Causa de Fórceps |
| Q175 | - |  |  | SI | Método de Inducción |
| Q176 | - |  |  | SI | Tipo de Anestesia (Parto) |
| Q177 | - |  |  | SI | Otra Anestesia (Parto) |
| Q178 | - |  |  | SI | Líqudo Amniótico |
| Q179 | - |  |  | SI | Placenta |
| Q180 | - |  |  | SI | Otros (Placenta) |
| Q181 | - |  |  | SI | Circular de Cordón |
| Q182 | - |  |  | SI | Complicaciones durante el Parto |
| Q183 | - |  |  | SI | Complicaciones Maternas |
| Q184 | - |  |  | SI | Complicaciones Fetales |
| Q185 | - |  |  | SI | Otras Complicaciones del Parto |
| Q186 | - |  |  | SI | Lugar del Parto |
| Q187 | - |  |  | SI | Otro Lugar de Parto |
| Q19 | - |  |  | SI | Pupilas |
| Q20 | - |  |  | SI | Ojos Comentarios |
| Q200 | - |  |  | SI | Piel Descripción |
| Q201 | - |  |  | SI | Lanugo Descripción |
| Q202 | - |  |  | SI | Hemangioms Descripción |
| Q203 | - |  |  | SI | Orejas Descripción |
| Q204 | - |  |  | SI | Cardiaco Descripción |
| Q205 | - |  |  | SI | Extremidades Descripción |
| Q206 | - |  |  | SI | Reflejo Descripción |
| Q22 | - |  |  | SI | Nariz Alterada |
| Q220 | - |  |  | SI | Administración Vacuna BCG: |
| Q221 | - |  |  | SI | Toma de PKU: |
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
| Q71 | - |  |  | SI | Extremidades Superiores Comentarios |
| Q72 | - |  |  | SI | Adecuadas en cuanto al tamaño y forma, dedos bien ... |
| Q74 | - |  |  | SI | Extremidades Inferiores Alteradas |
| Q75 | - |  |  | SI | Extremidades Inferiores Comentarios |
| Q76 | - |  |  | SI | Caderas simétricas, columna en postura adecuada pa... |
| Q78 | - |  |  | SI | Columna Alterada |
| Q79 | - |  |  | SI | Columna comentarios |
| Q80 | - |  |  | SI | Columna en postura adecuada para la edad, sin defo... |
| Q81 | - |  |  | SI | Actitud y Tono |
| Q84 | - |  |  | SI | Reflejos Arcaicos Ausentes |
| Q85 | - |  |  | SI | Reflejos Comentarios |
| Q86 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q87 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q88 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q89 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q90 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q91 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q92 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q93 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q94 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q95 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q96 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q97 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q98 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q99 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*