# SQLUser.ARC_PackageGroupSubType

**Schema:** SQLUser
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PKGRSTYPE_RowId | bigint | PK |  | NO | - |
| PKGRSTYPE_Code | varchar |  |  | NO | Code |
| PKGRSTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PKGRSTYPE_CreatedDate | date |  |  | SI | Created Date |
| PKGRSTYPE_CreatedTime | time |  |  | SI | Created Time |
| PKGRSTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PKGRSTYPE_DateFrom | date |  |  | SI | Date From |
| PKGRSTYPE_DateTo | date |  |  | SI | Date To |
| PKGRSTYPE_Desc | varchar |  |  | NO | Description |
| PKGRSTYPE_Owner | varchar |  |  | SI | Owner |
| PKGRSTYPE_PackGroupType_DR | bigint |  | FK | SI | Des Ref ARCPackageGroupType |
| PKGRSTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| PKGRSTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| PKGRSTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Datos del paciente |
| Q02 | - |  |  | SI | Talla (aproximada) |
| Q03 | - |  |  | SI | Peso (aproximado) |
| Q04 | - |  |  | SI | IMC |
| Q05 | - |  |  | SI | Tamizaje telefónico / Criterios de exclusión absol... |
| Q06 | - |  |  | SI | Criterios de exclusión absoluta que serán derivado... |
| Q07 | - |  |  | SI | Colonoscopia paciente ≥ 75 años |
| Q08 | - |  |  | SI | Endoscopia Paciente ≥ 80 años |
| Q09 | - |  |  | SI | Paciente ASA ≥ III |
| Q10 | - |  |  | SI | Paciente IMC ≥ 40 |
| Q11 | - |  |  | SI | Paciente alérgico al latex |
| Q12 | - |  |  | SI | Paciente alérgico a BZD |
| Q13 | - |  |  | SI | Embarazadas |
| Q14 | - |  |  | SI | Paciente en TACO |
| Q15 | - |  |  | SI | Pacientes >80 años * |
| Q16 | - |  |  | SI | En el caso del área dental se podrían atender paci... |
| Q17 | - |  |  | SI | Paciente sano con pase médico |
| Q18 | - |  |  | SI | CI de aprobación DO |
| Q19 | - |  |  | SI | aprobación Jefatura técnica dental |
| Q20 | - |  |  | SI | Paciente alérgico al látex |
| Q21 | - |  |  | SI | Pacientes con IMC > 40 |
| Q22 | - |  |  | SI | Encuesta |
| Q23 | - |  |  | SI | 1.Alergias |
| Q24 | - |  |  | SI | Observaciones |
| Q25 | - |  |  | SI | 2.Uso de anticoagulantes orales |
| Q26 | - |  |  | SI | Observaciones |
| Q27 | - |  |  | SI | 3.Uso de antiagregantes plaquetarios |
| Q28 | - |  |  | SI | Observaciones |
| Q29 | - |  |  | SI | 4.Diabetes Mellitus |
| Q30 | - |  |  | SI | Observaciones |
| Q31 | - |  |  | SI | a) Uso de hipoglicemiantes orales |
| Q32 | - |  |  | SI | Observaciones |
| Q33 | - |  |  | SI | b) Uso de insulina |
| Q34 | - |  |  | SI | Observaciones |
| Q35 | - |  |  | SI | 5.Hipertensión Arterial en tratamiento |
| Q36 | - |  |  | SI | Observaciones |
| Q37 | - |  |  | SI | 6.Cardiopatías congénitas, valvulares y/o marcapas... |
| Q38 | - |  |  | SI | Observaciones |
| Q39 | - |  |  | SI | 7.Paciente con infecciones de vías aéreas superior... |
| Q40 | - |  |  | SI | Observaciones |
| Q41 | - |  |  | SI | 8.Insuficiencia respiratoria, renal o hepática |
| Q42 | - |  |  | SI | Observaciones |
| Q43 | - |  |  | SI | 9.Obesidad mórbida (según IMC calculado) |
| Q44 | - |  |  | SI | Observaciones |
| Q45 | - |  |  | SI | Si encuesta fue aplicada por TENS, paciente que pr... |
| Q46 | - |  |  | SI | Se confirman indicaciones para día del procedimien... |
| Q47 | - |  |  | SI | Paciente debe presentarse 20 minutos antes de la h... |
| Q48 | - |  |  | SI | Llevar orden médica otorgada por profesional de Re... |
| Q49 | - |  |  | SI | Llevar cédula de identidad o pasaporte |
| Q50 | - |  |  | SI | Baño y/o Aseo especifico de la zona a intervenir |
| Q51 | - |  |  | SI | Reforzar Hora de presentación |
| Q52 | - |  |  | SI | Dar teléfono de contacto ante dudas |
| Q53 | - |  |  | SI | Si el paciente es menor de edad (18 años) siempre ... |
| Q54 | - |  |  | SI | Criterios de exclusión absoluta el día del exámen,... |
| Q55 | - |  |  | SI | Paciente febril >38° |
| Q56 | - |  |  | SI | Paciente ASA ≥ III |
| Q57 | - |  |  | SI | Alérgico al latex |
| Q58 | - |  |  | SI | Menor de edad sin tutor |
| Q59 | - |  |  | SI | Hematocrito menor 21% |
| Q60 | - |  |  | SI | Paciente IMC > 40 |
| Q61 | - |  |  | SI | Alérgico a anestésicos locales |
| Q62 | - |  |  | SI | Paciente en TACO |
| Q63 | - |  |  | SI | Sangramiento activo |
| Q64 | - |  |  | SI | PA > 160/100 |
| Q65 | - |  |  | SI | PA < 80/55 |
| Q66 | - |  |  | SI | HGT <70 y >250 |
| Q67 | - |  |  | SI | Dolor ≥7 |
| Q68 | - |  |  | SI | Condición clínica deteriorada |
| Q69 | - |  |  | SI | Fecha de contacto telefónico |
| Q70 | - |  |  | SI | TENS/Enfermera responsable |
| Q71 | - |  |  | SI | cm |
| Q72 | - |  |  | SI | kg |
| Q73 | - |  |  | SI | Paciente con patología de base y pase médico |
| Q74 | - |  |  | SI | Paciente sano con pase médico / Paciente con patol... |
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