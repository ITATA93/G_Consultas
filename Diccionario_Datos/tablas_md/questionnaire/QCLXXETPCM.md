# questionnaire.QCLXXETPCM

> Encuesta Telefónica Pabellón Cirugía Menor

**Schema:** questionnaire
**Columnas:** 115
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Encuesta Telefónica Pabellón Cirugía Menor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Datos del paciente |
| Q02 | numeric |  |  | SI | Talla (aproximada) |
| Q03 | numeric |  |  | SI | Peso (aproximado) |
| Q04 | varchar |  |  | SI | IMC |
| Q05 | varchar |  |  | SI | Tamizaje telefónico / Criterios de exclusión absol... |
| Q06 | varchar |  |  | SI | Criterios de exclusión absoluta que serán derivado... |
| Q07 | varchar |  |  | SI | Colonoscopia paciente ≥ 75 años |
| Q08 | varchar |  |  | SI | Endoscopia Paciente ≥ 80 años |
| Q09 | varchar |  |  | SI | Paciente ASA ≥ III |
| Q10 | varchar |  |  | SI | Paciente IMC ≥ 40 |
| Q11 | varchar |  |  | SI | Paciente alérgico al latex |
| Q12 | varchar |  |  | SI | Paciente alérgico a BZD |
| Q13 | varchar |  |  | SI | Embarazadas |
| Q14 | varchar |  |  | SI | Paciente en TACO |
| Q15 | varchar |  |  | SI | Pacientes >80 años * |
| Q16 | varchar |  |  | SI | En el caso del área dental se podrían atender paci... |
| Q17 | varchar |  |  | SI | Paciente sano con pase médico |
| Q18 | varchar |  |  | SI | CI de aprobación DO  |
| Q19 | varchar |  |  | SI | aprobación Jefatura técnica dental |
| Q20 | varchar |  |  | SI | Paciente alérgico al látex |
| Q21 | varchar |  |  | SI | Pacientes con IMC > 40 |
| Q22 | varchar |  |  | SI | Encuesta |
| Q23 | varchar |  |  | SI | 1.Alergias |
| Q24 | varchar |  |  | SI | Observaciones |
| Q25 | varchar |  |  | SI | 2.Uso de anticoagulantes orales |
| Q26 | varchar |  |  | SI | Observaciones |
| Q27 | varchar |  |  | SI | 3.Uso de antiagregantes plaquetarios |
| Q28 | varchar |  |  | SI | Observaciones |
| Q29 | varchar |  |  | SI | 4.Diabetes Mellitus |
| Q30 | varchar |  |  | SI | Observaciones |
| Q31 | varchar |  |  | SI | a) Uso de hipoglicemiantes orales |
| Q32 | varchar |  |  | SI | Observaciones |
| Q33 | varchar |  |  | SI | b) Uso de insulina |
| Q34 | varchar |  |  | SI | Observaciones |
| Q35 | varchar |  |  | SI | 5.Hipertensión Arterial en tratamiento |
| Q36 | varchar |  |  | SI | Observaciones |
| Q37 | varchar |  |  | SI | 6.Cardiopatías congénitas, valvulares y/o marcapas... |
| Q38 | varchar |  |  | SI | Observaciones |
| Q39 | varchar |  |  | SI | 7.Paciente con infecciones de vías aéreas superior... |
| Q40 | varchar |  |  | SI | Observaciones |
| Q41 | varchar |  |  | SI | 8.Insuficiencia respiratoria, renal o hepática |
| Q42 | varchar |  |  | SI | Observaciones |
| Q43 | varchar |  |  | SI | 9.Obesidad mórbida (según IMC calculado) |
| Q44 | varchar |  |  | SI | Observaciones |
| Q45 | varchar |  |  | SI | Si encuesta fue aplicada por TENS, paciente que pr... |
| Q46 | varchar |  |  | SI | Se confirman indicaciones para día del procedimien... |
| Q47 | varchar |  |  | SI | Paciente debe presentarse 20 minutos antes de la h... |
| Q48 | varchar |  |  | SI | Llevar orden médica otorgada por profesional de Re... |
| Q49 | varchar |  |  | SI | Llevar cédula de identidad o pasaporte |
| Q50 | varchar |  |  | SI | Baño y/o Aseo especifico de la zona a intervenir |
| Q51 | varchar |  |  | SI | Reforzar Hora de presentación |
| Q52 | varchar |  |  | SI | Dar teléfono de contacto ante dudas |
| Q53 | varchar |  |  | SI | Si el paciente es menor de edad (18 años) siempre ... |
| Q54 | varchar |  |  | SI | Criterios de exclusión absoluta el día del exámen,... |
| Q55 | varchar |  |  | SI | Paciente febril >38° |
| Q56 | varchar |  |  | SI | Paciente ASA ≥ III |
| Q57 | varchar |  |  | SI | Alérgico al latex |
| Q58 | varchar |  |  | SI | Menor de edad sin tutor |
| Q59 | varchar |  |  | SI | Hematocrito menor 21% |
| Q60 | varchar |  |  | SI | Paciente IMC > 40 |
| Q61 | varchar |  |  | SI | Alérgico a anestésicos locales |
| Q62 | varchar |  |  | SI | Paciente en TACO |
| Q63 | varchar |  |  | SI | Sangramiento activo |
| Q64 | varchar |  |  | SI | PA > 160/100 |
| Q65 | varchar |  |  | SI | PA < 80/55 |
| Q66 | varchar |  |  | SI | HGT <70 y >250 |
| Q67 | varchar |  |  | SI | Dolor ≥7 |
| Q68 | varchar |  |  | SI | Condición clínica deteriorada |
| Q69 | date |  |  | SI | Fecha de contacto telefónico |
| Q70 | varchar |  |  | SI | TENS/Enfermera responsable |
| Q71 | varchar |  |  | SI | cm |
| Q72 | varchar |  |  | SI | kg |
| Q73 | varchar |  |  | SI | Paciente con patología de base y pase médico |
| Q74 | varchar |  |  | SI | Paciente sano con pase médico / Paciente con patol... |
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