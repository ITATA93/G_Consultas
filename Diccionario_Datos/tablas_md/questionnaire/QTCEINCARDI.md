# questionnaire.QTCEINCARDI

> Ficha PS Cardiovascular

**Schema:** questionnaire
**Columnas:** 206
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha PS Cardiovascular

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Participa grupo comunitario: |
| Q02 | varchar |  |  | SI | Especificar: |
| Q04 | varchar |  |  | SI | Familiares 1 grado con enfermedad renal crónica: |
| Q05 | varchar |  |  | SI | Familiares 1 grado con muerte prematura por enferm... |
| Q06 | varchar |  |  | SI | Antecedentes personales de enfermedad cardiovascul... |
| Q07 | numeric |  |  | SI | Edad: |
| Q08 | varchar |  |  | SI | Complicaciones (marcar lo que corresponde e indica... |
| Q09 | varchar |  |  | SI | ACV |
| Q10 | varchar |  |  | SI | Otro |
| Q100 | date |  |  | SI | Fecha Electrocardiograma |
| Q101 | varchar |  |  | SI | Presión de Pulso |
| Q102 | varchar |  |  | SI | Paquetes/Año |
| Q105 | varchar |  |  | SI | Antecedentes Enf. Aterosclerótica |
| Q106 | varchar |  |  | SI | Creatinemia |
| Q106ObsDR | varchar |  | FK | SI | Creatinemia DR |
| Q107 | varchar |  |  | SI | PTGO 120m  |
| Q107ObsDR | varchar |  | FK | SI | PTGO 120m  DR |
| Q108 | date |  |  | SI | Fecha Creatinemia |
| Q109 | date |  |  | SI | Fecha PTGO 120m |
| Q11 | varchar |  |  | SI | IAM |
| Q110 | varchar |  |  | SI | Fondo de Ojo Derecho |
| Q110ObsDR | varchar |  | FK | SI | Fondo de Ojo Derecho DR |
| Q111 | varchar |  |  | SI | Fondo de Ojo Izquierdo |
| Q111ObsDR | varchar |  | FK | SI | Fondo de Ojo Izquierdo DR |
| Q112 | varchar |  |  | SI | RAC |
| Q112ObsDR | varchar |  | FK | SI | RAC DR |
| Q113 | date |  |  | SI | Fecha RAC |
| Q114 | varchar |  |  | SI | Creatinuria |
| Q114ObsDR | varchar |  | FK | SI | Creatinuria DR |
| Q115 | numeric |  |  | SI | N° Tragos x Semana |
| Q116 | varchar |  |  | SI | Alcoholismo |
| Q117 | varchar |  |  | SI | Con Amputación por Pie Diabético |
| Q118 | varchar |  |  | SI | Con Atención Podológica Vigente |
| Q119 | varchar |  |  | SI | Protocolo HEARTS |
| Q12 | varchar |  |  | SI | Tabaquismo |
| Q120 | varchar |  |  | SI | Enfermedad Renal Crónica |
| Q121 | varchar |  |  | SI | Etapa HEARTS |
| Q122 | date |  |  | SI | Fecha Inicio HEARTS |
| Q123 | date |  |  | SI | Fecha Fin HEARTS |
| Q13 | numeric |  |  | SI | N cigarrillos día: |
| Q14 | numeric |  |  | SI | N de años de tabaquismo activo |
| Q15 | varchar |  |  | SI | Hipertensión Arterial |
| Q16hiper | varchar |  |  | SI | Fámacos: |
| Q17Dia | varchar |  |  | SI | Fámacos: |
| Q18dis | varchar |  |  | SI | Fámacos: |
| Q19 | varchar |  |  | SI | Otros antecedentes: |
| Q20 | varchar |  |  | SI | Diabetes |
| Q21 | varchar |  |  | SI | Dislipidemia |
| Q22 | varchar |  |  | SI | Peso |
| Q22ObsDR | varchar |  | FK | SI | Peso DR |
| Q23 | varchar |  |  | SI | Talla |
| Q23ObsDR | varchar |  | FK | SI | Talla DR |
| Q24 | varchar |  |  | SI | IMC |
| Q24ObsDR | varchar |  | FK | SI | IMC DR |
| Q25 | varchar |  |  | SI | CC |
| Q25ObsDR | varchar |  | FK | SI | CC DR |
| Q26 | varchar |  |  | SI | Obesidad central: |
| Q27 | varchar |  |  | SI | P. Arterial Sistólica |
| Q27ObsDR | varchar |  | FK | SI | P. Arterial Sistólica DR |
| Q28 | varchar |  |  | SI | P.Diastolica de Pie |
| Q28ObsDR | varchar |  | FK | SI | P.Diastolica de Pie DR |
| Q29 | varchar |  |  | SI | Frecuencia Cardíaca |
| Q29ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca DR |
| Q30 | varchar |  |  | SI | Presión de Pulso |
| Q30ObsDR | varchar |  | FK | SI | Presión de Pulso DR |
| Q31 | varchar |  |  | SI | Descripción hallazgos encontrados: |
| Q32 | numeric |  |  | SI | Pie Derecho: |
| Q33 | numeric |  |  | SI | Pie Izquierdo: |
| Q34 | numeric |  |  | SI | Pulsos dístales: |
| Q35 | varchar |  |  | SI | Diagnóstico(s): |
| Q36 | date |  |  | SI | Fecha: |
| Q37 | varchar |  |  | SI | Glicemia |
| Q37ObsDR | varchar |  | FK | SI | Glicemia DR |
| Q38 | varchar |  |  | SI | PTGO |
| Q38ObsDR | varchar |  | FK | SI | PTGO DR |
| Q39 | varchar |  |  | SI | HbA1c |
| Q39ObsDR | varchar |  | FK | SI | HbA1c DR |
| Q40 | varchar |  |  | SI | Creatínina |
| Q40ObsDR | varchar |  | FK | SI | Creatínina DR |
| Q41 | varchar |  |  | SI | Colesterol Total |
| Q41ObsDR | varchar |  | FK | SI | Colesterol Total DR |
| Q42 | varchar |  |  | SI | Colesterol HDL |
| Q42ObsDR | varchar |  | FK | SI | Colesterol HDL DR |
| Q43 | varchar |  |  | SI | Colesterol LDL |
| Q44 | varchar |  |  | SI | Triglicéridos: |
| Q44ObsDR | varchar |  | FK | SI | Triglicéridos: DR |
| Q45 | varchar |  |  | SI | Proteinuria: |
| Q46 | varchar |  |  | SI | Hematuria: |
| Q47 | varchar |  |  | SI | Cilindros: |
| Q48 | varchar |  |  | SI | Microalbuminuria |
| Q48ObsDR | varchar |  | FK | SI | Microalbuminuria DR |
| Q49 | varchar |  |  | SI | Fondo de ojo: |
| Q49ObsDR | varchar |  | FK | SI | Fondo de ojo: DR |
| Q50 | varchar |  |  | SI | ECG Hipertrofia ventricular izquerda: |
| Q51 | varchar |  |  | SI | Otros Hallazgos: |
| Q52 | numeric |  |  | SI | VFGe: |
| Q53 | varchar |  |  | SI | Riesgo Cardio vascular |
| Q54 | varchar |  |  | SI | VFGE: |
| Q55 | numeric |  |  | SI | Informada Lab: |
| Q56 | varchar |  |  | SI | Calculado Mujer: |
| Q57 | varchar |  |  | SI | Calculado Hombre: |
| Q58 | varchar |  |  | SI | P. Arterial Diastólica |
| Q58ObsDR | varchar |  | FK | SI | P. Arterial Diastólica DR |
| Q59 | varchar |  |  | SI | P.Sistolica de Pie |
| Q59ObsDR | varchar |  | FK | SI | P.Sistolica de Pie DR |
| Q60 | varchar |  |  | SI | IMC (Calcuado) |
| Q61 | varchar |  |  | SI | Glucosa 60 Min. |
| Q61ObsDR | varchar |  | FK | SI | Glucosa 60 Min. DR |
| Q62 | varchar |  |  | SI | Glucosa Basal |
| Q62ObsDR | varchar |  | FK | SI | Glucosa Basal DR |
| Q63 | numeric |  |  | SI | Glucosa 120 Min. |
| Q64 | varchar |  |  | SI | Calculado Mujer Raza |
| Q65 | varchar |  |  | SI | Calculado Hombre Raza |
| Q66 | varchar |  |  | SI | Porcentaje Riesgo Cardiovascular |
| Q66ObsDR | varchar |  | FK | SI | Porcentaje Riesgo Cardiovascular DR |
| Q67 | varchar |  |  | SI | Riesgo Cardiovascular |
| Q68 | varchar |  |  | SI | Resultado Riesgo Ulceración Pié Diabético |
| Q68ObsDR | varchar |  | FK | SI | Resultado Riesgo Ulceración Pié Diabético DR |
| Q69 | varchar |  |  | SI | Resultado Pauta de Enfermedad Renal Crónica |
| Q69ObsDR | varchar |  | FK | SI | Resultado Pauta de Enfermedad Renal Crónica DR |
| Q70 | varchar |  |  | SI | Edad Paciente |
| Q72 | varchar |  |  | SI | Estado Nutricional |
| Q72ObsDR | varchar |  | FK | SI | Estado Nutricional DR |
| Q73 | varchar |  |  | SI | Intolerancia a la Glucosa |
| Q73ObsDR | varchar |  | FK | SI | Intolerancia a la Glucosa DR |
| Q74 | varchar |  |  | SI | Electrocardiograma |
| Q74ObsDR | varchar |  | FK | SI | Electrocardiograma DR |
| Q75 | varchar |  |  | SI | TSH |
| Q75ObsDR | varchar |  | FK | SI | TSH DR |
| Q76 | varchar |  |  | SI | PAP |
| Q76ObsDR | varchar |  | FK | SI | PAP DR |
| Q77 | varchar |  |  | SI | Sedentarismo |
| Q77ObsDR | varchar |  | FK | SI | Sedentarismo DR |
| Q78 | varchar |  |  | SI | Colesterol LDL |
| Q78ObsDR | varchar |  | FK | SI | Colesterol LDL DR |
| Q80 | varchar |  |  | SI | Velocidad de Filtración Glomerular |
| Q80ObsDR | varchar |  | FK | SI | Velocidad de Filtración Glomerular DR |
| Q81 | varchar |  |  | SI | Riesgo Ulceración Pie Diabético Derecho |
| Q81ObsDR | varchar |  | FK | SI | Riesgo Ulceración Pie Diabético Derecho DR |
| Q82 | varchar |  |  | SI | Riesgo Ulceración Pie Diabético Izquierdo |
| Q82ObsDR | varchar |  | FK | SI | Riesgo Ulceración Pie Diabético Izquierdo DR |
| Q83 | varchar |  |  | SI | Etapa Enfermedad Renal Crónica |
| Q83ObsDR | varchar |  | FK | SI | Etapa Enfermedad Renal Crónica DR |
| Q84 | varchar |  |  | SI | EFAM A |
| Q84ObsDR | varchar |  | FK | SI | EFAM A DR |
| Q85 | varchar |  |  | SI | EFAM B |
| Q85ObsDR | varchar |  | FK | SI | EFAM B DR |
| Q86 | date |  |  | SI | Fecha Colesterol Total |
| Q87 | date |  |  | SI | Fecha Colesterol HDL |
| Q88 | date |  |  | SI | Fecha Triglicéridos |
| Q89 | date |  |  | SI | Fecha Glicemia |
| Q90 | date |  |  | SI | Fecha HbA1c |
| Q91 | date |  |  | SI | Fecha PTGO |
| Q92 | date |  |  | SI | Fecha Proteinuria |
| Q93 | date |  |  | SI | Fecha Cilindros |
| Q94 | date |  |  | SI | Fecha Hematuria |
| Q95 | date |  |  | SI | Fecha Microalbuminuria |
| Q96 | date |  |  | SI | Fecha Creatinina |
| Q97 | date |  |  | SI | Fecha TSH |
| Q98 | date |  |  | SI | Fecha Fondo de Ojo |
| Q99 | date |  |  | SI | Fecha PAP |
| QAFA | varchar |  |  | SI | Actividad Física Actual |
| QAFF | numeric |  |  | SI | Actividad Física Frecuencia |
| QSED | varchar |  |  | SI | Sedentario |
| QSEDObsDR | varchar |  | FK | SI | Sedentario DR |
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