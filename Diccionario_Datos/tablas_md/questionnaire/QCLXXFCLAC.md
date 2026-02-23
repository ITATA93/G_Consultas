# questionnaire.QCLXXFCLAC

> Ficha de Ingreso Clínica de Lactancia

**Schema:** questionnaire
**Columnas:** 153
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha de Ingreso Clínica de Lactancia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | N° Ficha:&nbsp; |
| Q02 | varchar |  |  | SI | Nombre de la Madre |
| Q03 | numeric |  |  | SI | Edad de la Madre |
| Q04 | varchar |  |  | SI | Nivel Educacional&nbsp; |
| Q05 | numeric |  |  | SI | Número de hijos |
| Q06 | varchar |  |  | SI | Tiempo duración de lactancia anterior |
| Q07 | varchar |  |  | SI | Acompañante de la Madre |
| Q08 | varchar |  |  | SI | Nombre del RN y/o Lactante |
| Q09 | varchar |  |  | SI | Apellido&nbsp; del RN y/o Lactante |
| Q10 | varchar |  |  | SI | Apellido Materno&nbsp;Apellido&nbsp; del RN y/o La... |
| Q100 | varchar |  |  | SI | Edad Gestacional al Nacer |
| Q100ObsDR | varchar |  | FK | SI | Edad Gestacional al Nacer DR |
| Q101 | varchar |  |  | SI | Edad |
| Q102 | varchar |  |  | SI | Peso/Talla |
| Q102ObsDR | varchar |  | FK | SI | Peso/Talla DR |
| Q11 | varchar |  |  | SI | ANTECEDENTES DEL NIÑO NIÑA |
| Q12 | varchar |  |  | SI | Edad cronológica&nbsp; |
| Q13 | varchar |  |  | SI | Edad cronológica&nbsp; |
| Q14 | varchar |  |  | SI | Edad corregida |
| Q14ObsDR | varchar |  | FK | SI | Edad corregida DR |
| Q15 | varchar |  |  | SI | Perímetro Craneano al nacer |
| Q15ObsDR | varchar |  | FK | SI | Perímetro Craneano al nacer DR |
| Q16 | varchar |  |  | SI | Circunferencia Craneana |
| Q16ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q17 | varchar |  |  | SI | Peso actual |
| Q17ObsDR | varchar |  | FK | SI | Peso actual DR |
| Q18 | numeric |  |  | SI | Peso anterior |
| Q19 | numeric |  |  | SI | Incremento ponderal promedio día (gr): |
| Q20 | numeric |  |  | SI | Longitud (cm) |
| Q21 | varchar |  |  | SI | Peso/Edad |
| Q21ObsDR | varchar |  | FK | SI | Peso/Edad DR |
| Q22 | varchar |  |  | SI | Talla/Edad |
| Q22ObsDR | varchar |  | FK | SI | Talla/Edad DR |
| Q23 | varchar |  |  | SI | Diagnóstico nutricional |
| Q23ObsDR | varchar |  | FK | SI | Diagnóstico nutricional DR |
| Q24 | varchar |  |  | SI | TIPO DE ALIMENTACIÓN NIÑO/A |
| Q25 | varchar |  |  | SI | Tipo de Alimentación del Niño/a |
| Q25ObsDR | varchar |  | FK | SI | Tipo de Alimentación del Niño/a DR |
| Q26 | varchar |  |  | SI | Formula |
| Q27 | varchar |  |  | SI | Motivo del inicio de Lactancia Artificial |
| Q28 | varchar |  |  | SI | EXAMEN FÍSICO DEL PACTANTE Y REFLEJOS DE LACTANCIA |
| Q29 | varchar |  |  | SI | Micosis en cavidad oral |
| Q30 | varchar |  |  | SI | Dientes |
| Q31 | varchar |  |  | SI | Frenillos |
| Q32 | varchar |  |  | SI | Ictericia |
| Q33 | varchar |  |  | SI | Dermatitis del pañal |
| Q34 | varchar |  |  | SI | Signos de deshidratación |
| Q35 | varchar |  |  | SI | Reflejo de búsqueda del pezón y apertura de la boc... |
| Q36 | varchar |  |  | SI | Reflejo de protrusión lingual |
| Q37 | varchar |  |  | SI | Reflejo de succión |
| Q38 | varchar |  |  | SI | Reflejo de deglución |
| Q39 | varchar |  |  | SI | Reflejo de extrusión |
| Q40 | varchar |  |  | SI | Paladar duro y blando |
| Q41 | varchar |  |  | SI | EXÁMENES FÍSICO DE MAMAS Y PEZÓN |
| Q42 | varchar |  |  | SI | Congestión |
| Q43 | varchar |  |  | SI | Induración local |
| Q44 | varchar |  |  | SI | Dolor a la palpación |
| Q45 | varchar |  |  | SI | Dolor al amamantar |
| Q46 | varchar |  |  | SI | Aumento de temperatura |
| Q47 | varchar |  |  | SI | Signos de deshidratación |
| Q48 | varchar |  |  | SI | Enrojecimiento |
| Q49 | varchar |  |  | SI | Micosis de pezón |
| Q50 | varchar |  |  | SI | Reflejo eyecto láctico |
| Q51 | varchar |  |  | SI | Grietas en pezón |
| Q52 | varchar |  |  | SI | Pezón plano/invertido |
| Q53 | varchar |  |  | SI | Paladar duro y blando |
| Q54 | varchar |  |  | SI | ANTECEDENTES MORBIDOS |
| Q55 | varchar |  |  | SI | Prematuro tardío |
| Q56 | varchar |  |  | SI | Recién Nacido Pre-Término o Muy Bajo Peso al Nacer |
| Q57 | varchar |  |  | SI | Asfixia perinatal y/o Parálisis Cerebral |
| Q58 | varchar |  |  | SI | Baja de peso al alta &gt; 10%: |
| Q59 | varchar |  |  | SI | Madre obesa |
| Q60 | varchar |  |  | SI | Cromosomopatía o genopatía |
| Q61 | varchar |  |  | SI | ANAMNESIS LACTANCIA |
| Q62 | varchar |  |  | SI | Tipo de parto |
| Q63 | varchar |  |  | SI | Tipo de analgesia en parto |
| Q64 | varchar |  |  | SI | Hubo acoplamiento espontáneo |
| Q65 | varchar |  |  | SI | Hubo alojamiento conjunto |
| Q66 | varchar |  |  | SI | Inicio del apego (horas): |
| Q67 | varchar |  |  | SI | Nº horas postparto para primera puesta al pecho |
| Q68 | varchar |  |  | SI | Frecuencia mamada |
| Q69 | varchar |  |  | SI | Mamada ambos pechos por vez |
| Q70 | varchar |  |  | SI | Mamadas nocturnas número |
| Q71 | varchar |  |  | SI | Tiempo transcurrido entre mamadas |
| Q72 | varchar |  |  | SI | Tipo técnica amamantamiento |
| Q73 | varchar |  |  | SI | Ingesta relleno del lactante |
| Q74 | varchar |  |  | SI | Uso de chupete de entretención |
| Q75 | numeric |  |  | SI | Número pañales mojados (mínimo 6 |
| Q76 | varchar |  |  | SI | Apoyo del padre (u otros) |
| Q77 | varchar |  |  | SI | Madre trabaja fuera del hogar |
| Q78 | varchar |  |  | SI | Patología asociada de la madre |
| Q79 | varchar |  |  | SI | Patología asociada del lactante |
| Q80 | varchar |  |  | SI | Antecedente de problemas de lactancia |
| Q81 | varchar |  |  | SI | OTROS ANTECEDENTES |
| Q82 | varchar |  |  | SI | Madre adolescente |
| Q83 | varchar |  |  | SI | Actitud materna poco proclive a LM |
| Q84 | varchar |  |  | SI | Madre con consumo de sustancias (tabaco, alcohol, ... |
| Q85 | varchar |  |  | SI | Sospecha Depresión post parto y/o antecedentes de ... |
| Q86 | varchar |  |  | SI | Hospitalización en el menor de 3 meses |
| Q87 | varchar |  |  | SI | Indicación de relleno al alta |
| Q88 | varchar |  |  | SI | USO DE FÁRMACOS EN MADRE Y LACTANTE |
| Q89 | varchar |  |  | SI | Uso de fármacos en madre y lactante |
| Q90 | varchar |  |  | SI | INDICACIONES PARA EL LACTANTE |
| Q91 | varchar |  |  | SI | Indicaciones para el lactante |
| Q92 | varchar |  |  | SI | INDICACIONES PARA LA MADRE |
| Q93 | varchar |  |  | SI | Indicaciones para la madre |
| Q94 | varchar |  |  | SI | CITACIÓN A CONTROL DEL LACTANTE |
| Q95 | varchar |  |  | SI | Citación a control del lactante |
| Q96 | varchar |  |  | SI | OTROS ANTECEDENTES |
| Q97 | varchar |  |  | SI | Otros antecedentes |
| Q98 | varchar |  |  | SI | Nombre Profesional |
| Q99 | varchar |  |  | SI | RUN |
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