# questionnaire.QTCEEXFINEO

> Ingreso Médico Neonatología

**Schema:** questionnaire
**Columnas:** 196
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Médico Neonatología

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit |  |  | SI | Flexión esperada para la edad, con movimientos act... |
| Q02 | varchar |  |  | SI | Piel |
| Q03 | varchar |  |  | SI | Lanugo |
| Q04 | varchar |  |  | SI | Comentarios actitud general |
| Q06 | varchar |  |  | SI | Comentario Hemangiomas |
| Q07 | varchar |  |  | SI | Mancha Mongólica |
| Q08 | varchar |  |  | SI | Descripción Mancha Mongólica |
| Q10 | bit |  |  | SI | Cráneo simétrico, sin deformidades ni cefalohemato... |
| Q100 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q101 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q102 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q103 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q104 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q105 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q106 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q107 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q108 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q109 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q11 | varchar |  |  | SI | Cráneo Alterado |
| Q110 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q111 | date |  |  | SI | Fecha de Ingreso |
| Q112 | time |  |  | SI | Hora de Ingreso |
| Q114 | varchar |  |  | SI | Información entregada por |
| Q115 | varchar |  |  | SI | Contacto |
| Q116 | varchar |  |  | SI | Procedencia del paciente |
| Q117 | varchar |  |  | SI | Procedencia, descripción |
| Q12 | varchar |  |  | SI | Cráneo Alterado Comentarios |
| Q120 | varchar |  |  | SI | Anamnésis Próxima |
| Q121 | varchar |  |  | SI | Conclusiones |
| Q122 | varchar |  |  | SI | Plan de Manejo al Ingreso |
| Q123 | varchar |  |  | SI | Profesional de Salud |
| Q124 | varchar |  |  | SI | Fono Contacto |
| Q125 | date |  |  | SI | Fecha Nacimiento |
| Q126 | time |  |  | SI | Hora de Nacimiento |
| Q129 | varchar |  |  | SI | Sexo |
| Q130 | varchar |  |  | SI | Peso al Nacer |
| Q130ObsDR | varchar |  | FK | SI | Peso al Nacer DR |
| Q131 | varchar |  |  | SI | Talla al Nacer |
| Q131ObsDR | varchar |  | FK | SI | Talla al Nacer DR |
| Q132 | varchar |  |  | SI | Circunferencia Craneana |
| Q132ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q134 | varchar |  |  | SI | Apego |
| Q135 | varchar |  |  | SI | Apego Duración |
| Q14 | bit |  |  | SI | Fascie no característica, sin asimetrías ni paráli... |
| Q141 | varchar |  |  | SI | Diuresis |
| Q143 | varchar |  |  | SI | Deposiciones |
| Q144 | varchar |  |  | SI | Lactancia Materna |
| Q145 | varchar |  |  | SI | Alimentación Complementaria |
| Q146 | varchar |  |  | SI | Administración Vitamina  K |
| Q147 | varchar |  |  | SI | Alimentación Complementaria |
| Q148 | varchar |  |  | SI | Reanimación |
| Q149 | varchar |  |  | SI | Profilaxis Ocular |
| Q15 | varchar |  |  | SI | Cara Comentarios |
| Q150 | varchar |  |  | SI | Anomalía Congénita |
| Q152 | varchar |  |  | SI | Muestra de Sangre de Cordón Grupo RH Coomb |
| Q153 | numeric |  |  | SI | Semanas de Gestación 1 |
| Q154 | numeric |  |  | SI | Semanas de Gestación 2 |
| Q155 | varchar |  |  | SI | Morbilidad RN |
| Q156 | varchar |  |  | SI | Apgar 1 Minuto |
| Q157 | varchar |  |  | SI | Apgar 5 Minutos |
| Q158 | varchar |  |  | SI | Apgar 10 Minutos |
| Q159 | varchar |  |  | SI | Nombre de la Madre |
| Q160 | numeric |  |  | SI | Edad Materna |
| Q161 | varchar |  |  | SI | Gesta |
| Q162 | numeric |  |  | SI | Número de Partos |
| Q163 | numeric |  |  | SI | Hijos Vivos |
| Q164 | varchar |  |  | SI | Grupo Sanguíneo Materno |
| Q165 | varchar |  |  | SI | Factor RH Materno |
| Q17 | bit |  |  | SI | No presenta hemangiomas subconjuntivales. Pupilas ... |
| Q170 | varchar |  |  | SI | Patología del Embarazo |
| Q171 | varchar |  |  | SI | Medicamentos que tomó durante el embarazo |
| Q172 | varchar |  |  | SI | Tipo de Parto  |
| Q173 | varchar |  |  | SI | Causa de Cesárea |
| Q174 | varchar |  |  | SI | Causa de Fórceps |
| Q175 | varchar |  |  | SI | Método de Inducción |
| Q176 | varchar |  |  | SI | Tipo de Anestesia (Parto) |
| Q177 | varchar |  |  | SI | Otra Anestesia (Parto) |
| Q178 | varchar |  |  | SI | Líqudo Amniótico |
| Q179 | varchar |  |  | SI | Placenta |
| Q180 | varchar |  |  | SI | Otros (Placenta) |
| Q181 | varchar |  |  | SI | Circular de Cordón |
| Q182 | varchar |  |  | SI | Complicaciones durante el Parto |
| Q183 | varchar |  |  | SI | Complicaciones Maternas |
| Q184 | varchar |  |  | SI | Complicaciones Fetales |
| Q185 | varchar |  |  | SI | Otras Complicaciones del Parto |
| Q186 | varchar |  |  | SI | Lugar del Parto |
| Q187 | varchar |  |  | SI | Otro Lugar de Parto |
| Q19 | varchar |  |  | SI | Pupilas |
| Q20 | varchar |  |  | SI | Ojos Comentarios |
| Q200 | varchar |  |  | SI | Piel Descripción |
| Q201 | varchar |  |  | SI | Lanugo Descripción |
| Q202 | varchar |  |  | SI | Hemangioms Descripción |
| Q203 | varchar |  |  | SI | Orejas Descripción |
| Q204 | varchar |  |  | SI | Cardiaco Descripción |
| Q205 | varchar |  |  | SI | Extremidades Descripción |
| Q206 | varchar |  |  | SI | Reflejo Descripción |
| Q22 | varchar |  |  | SI | Nariz Alterada |
| Q220 | varchar |  |  | SI | Administración Vacuna BCG:  |
| Q221 | varchar |  |  | SI | Toma de PKU:  |
| Q23 | varchar |  |  | SI | Nariz Comentarios |
| Q24 | bit |  |  | SI | Adecuada para la edad, sin estridor, ni atresia de... |
| Q26 | bit |  |  | SI | Cavidad bucal adecuada para la edad, no presenta d... |
| Q27 | varchar |  |  | SI | Boca alterada |
| Q28 | varchar |  |  | SI | Boca Comentarios |
| Q31 | varchar |  |  | SI | Orejas Comentarios |
| Q32 | bit |  |  | SI | Pabellones auriculares adecuados para la edad, no ... |
| Q34 | varchar |  |  | SI | Cuello Alterado |
| Q35 | varchar |  |  | SI | Cuello Comentario |
| Q36 | bit |  |  | SI | Región cervical adecuada, no presenta tortícolis, ... |
| Q39 | varchar |  |  | SI | Pulmonar Comentarios |
| Q40 | bit |  |  | SI | Adecuado para la edad, cilíndrico, blando, murmull... |
| Q43 | bit |  |  | SI | Ritmo regular en dos tiempos, sin ruidos agregados... |
| Q45 | varchar |  |  | SI | Clavícula Alterada |
| Q46 | varchar |  |  | SI | Clavicula Comentarios |
| Q47 | bit |  |  | SI | Clavículas simétricas, sin signos de lesión |
| Q49 | varchar |  |  | SI | Mamas Comentarios |
| Q50 | bit |  |  | SI | Areola completa, glándula presente. |
| Q53 | varchar |  |  | SI | Abdomen Comentarios |
| Q54 | bit |  |  | SI | Abdomen simétrico, depresible, ruidos hidroaéreos ... |
| Q56 | varchar |  |  | SI | Ombligo Alterado |
| Q57 | varchar |  |  | SI | Ombligo comentarios |
| Q58 | bit |  |  | SI | Rosado, sin hernias, tres vasos. |
| Q59 | varchar |  |  | SI | Genitales Masculinos Comentarios |
| Q60 | varchar |  |  | SI | Genitales Masculinos alterados |
| Q61 | bit |  |  | SI | Genitales masculinos adecuados para la edad, testí... |
| Q63 | varchar |  |  | SI | Genitales Femeninos Comentarios |
| Q64 | bit |  |  | SI | Genitales femeninos adecuados para la edad, labios... |
| Q66 | varchar |  |  | SI | Ano anormal |
| Q67 | varchar |  |  | SI | Comentario ano |
| Q68 | bit |  |  | SI | Ano con esfínter funcional, sin fístulas. |
| Q71 | varchar |  |  | SI | Extremidades Superiores Comentarios |
| Q72 | bit |  |  | SI | Adecuadas en cuanto al tamaño y forma, dedos bien ... |
| Q74 | varchar |  |  | SI | Extremidades Inferiores Alteradas |
| Q75 | varchar |  |  | SI | Extremidades Inferiores Comentarios |
| Q76 | bit |  |  | SI | Caderas simétricas, columna en postura adecuada pa... |
| Q78 | varchar |  |  | SI | Columna Alterada |
| Q79 | varchar |  |  | SI | Columna comentarios |
| Q80 | bit |  |  | SI | Columna en postura adecuada para la edad, sin defo... |
| Q81 | varchar |  |  | SI | Actitud y Tono |
| Q84 | bit |  |  | SI | Reflejos Arcaicos Ausentes |
| Q85 | varchar |  |  | SI | Reflejos Comentarios |
| Q86 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q87 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q88 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q89 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q90 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q91 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q92 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q93 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q94 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q95 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q96 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q97 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q98 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q99 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*