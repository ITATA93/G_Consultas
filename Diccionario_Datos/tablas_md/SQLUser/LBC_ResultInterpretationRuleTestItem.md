# SQLUser.LBC_ResultInterpretationRuleTestItem

**Schema:** SQLUser
**Columnas:** 210
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRIRTI_ParRef | varchar | PK |  | NO | Parent Result Interpretation Rule |
| LBCRIRTI_Operator | varchar |  |  | NO | Operator |
| LBCRIRTI_ResultValue | varchar |  |  | SI | Result Value |
| LBCRIRTI_ResultValue2 | varchar |  |  | SI | Secondary Result Value for In Range Operator [a,b] |
| LBCRIRTI_Result_DR | varchar |  | FK | SI | Result  |
| LBCRIRTI_RowID | varchar |  |  | NO | - |
| LBCRIRTI_TestSetRevisionItem_DR | varchar |  | FK | SI | Test Set Revision Item
To support progressive loa... |
| Q01 | - |  |  | SI | Participa grupo comunitario: |
| Q02 | - |  |  | SI | Especificar: |
| Q04 | - |  |  | SI | Familiares 1 grado con enfermedad renal crónica: |
| Q05 | - |  |  | SI | Familiares 1 grado con muerte prematura por enferm... |
| Q06 | - |  |  | SI | Antecedentes personales de enfermedad cardiovascul... |
| Q07 | - |  |  | SI | Edad: |
| Q08 | - |  |  | SI | Complicaciones (marcar lo que corresponde e indica... |
| Q09 | - |  |  | SI | ACV |
| Q10 | - |  |  | SI | Otro |
| Q100 | - |  |  | SI | Fecha Electrocardiograma |
| Q101 | - |  |  | SI | Presión de Pulso |
| Q102 | - |  |  | SI | Paquetes/Año |
| Q105 | - |  |  | SI | Antecedentes Enf. Aterosclerótica |
| Q106 | - |  |  | SI | Creatinemia |
| Q106ObsDR | - |  |  | SI | Creatinemia DR |
| Q107 | - |  |  | SI | PTGO 120m |
| Q107ObsDR | - |  |  | SI | PTGO 120m  DR |
| Q108 | - |  |  | SI | Fecha Creatinemia |
| Q109 | - |  |  | SI | Fecha PTGO 120m |
| Q11 | - |  |  | SI | IAM |
| Q110 | - |  |  | SI | Fondo de Ojo Derecho |
| Q110ObsDR | - |  |  | SI | Fondo de Ojo Derecho DR |
| Q111 | - |  |  | SI | Fondo de Ojo Izquierdo |
| Q111ObsDR | - |  |  | SI | Fondo de Ojo Izquierdo DR |
| Q112 | - |  |  | SI | RAC |
| Q112ObsDR | - |  |  | SI | RAC DR |
| Q113 | - |  |  | SI | Fecha RAC |
| Q114 | - |  |  | SI | Creatinuria |
| Q114ObsDR | - |  |  | SI | Creatinuria DR |
| Q115 | - |  |  | SI | N° Tragos x Semana |
| Q116 | - |  |  | SI | Alcoholismo |
| Q117 | - |  |  | SI | Con Amputación por Pie Diabético |
| Q118 | - |  |  | SI | Con Atención Podológica Vigente |
| Q119 | - |  |  | SI | Protocolo HEARTS |
| Q12 | - |  |  | SI | Tabaquismo |
| Q120 | - |  |  | SI | Enfermedad Renal Crónica |
| Q13 | - |  |  | SI | N cigarrillos día: |
| Q14 | - |  |  | SI | N de años de tabaquismo activo |
| Q15 | - |  |  | SI | Hipertensión Arterial |
| Q16hiper | - |  |  | SI | Fámacos: |
| Q17Dia | - |  |  | SI | Fámacos: |
| Q18dis | - |  |  | SI | Fámacos: |
| Q19 | - |  |  | SI | Otros antecedentes: |
| Q20 | - |  |  | SI | Diabetes |
| Q21 | - |  |  | SI | Dislipidemia |
| Q22 | - |  |  | SI | Peso |
| Q22ObsDR | - |  |  | SI | Peso DR |
| Q23 | - |  |  | SI | Talla |
| Q23ObsDR | - |  |  | SI | Talla DR |
| Q24 | - |  |  | SI | IMC |
| Q24ObsDR | - |  |  | SI | IMC DR |
| Q25 | - |  |  | SI | CC |
| Q25ObsDR | - |  |  | SI | CC DR |
| Q26 | - |  |  | SI | Obesidad central: |
| Q27 | - |  |  | SI | P. Arterial Sistólica |
| Q27ObsDR | - |  |  | SI | P. Arterial Sistólica DR |
| Q28 | - |  |  | SI | P.Diastolica de Pie |
| Q28ObsDR | - |  |  | SI | P.Diastolica de Pie DR |
| Q29 | - |  |  | SI | Frecuencia Cardíaca |
| Q29ObsDR | - |  |  | SI | Frecuencia Cardíaca DR |
| Q30 | - |  |  | SI | Presión de Pulso |
| Q30ObsDR | - |  |  | SI | Presión de Pulso DR |
| Q31 | - |  |  | SI | Descripción hallazgos encontrados: |
| Q32 | - |  |  | SI | Pie Derecho: |
| Q33 | - |  |  | SI | Pie Izquierdo: |
| Q34 | - |  |  | SI | Pulsos dístales: |
| Q35 | - |  |  | SI | Diagnóstico(s): |
| Q36 | - |  |  | SI | Fecha: |
| Q37 | - |  |  | SI | Glicemia |
| Q37ObsDR | - |  |  | SI | Glicemia DR |
| Q38 | - |  |  | SI | PTGO |
| Q38ObsDR | - |  |  | SI | PTGO DR |
| Q39 | - |  |  | SI | HbA1c |
| Q39ObsDR | - |  |  | SI | HbA1c DR |
| Q40 | - |  |  | SI | Creatínina |
| Q40ObsDR | - |  |  | SI | Creatínina DR |
| Q41 | - |  |  | SI | Colesterol Total |
| Q41ObsDR | - |  |  | SI | Colesterol Total DR |
| Q42 | - |  |  | SI | Colesterol HDL |
| Q42ObsDR | - |  |  | SI | Colesterol HDL DR |
| Q43 | - |  |  | SI | Colesterol LDL |
| Q44 | - |  |  | SI | Triglicéridos: |
| Q44ObsDR | - |  |  | SI | Triglicéridos: DR |
| Q45 | - |  |  | SI | Proteinuria: |
| Q46 | - |  |  | SI | Hematuria: |
| Q47 | - |  |  | SI | Cilindros: |
| Q48 | - |  |  | SI | Microalbuminuria |
| Q48ObsDR | - |  |  | SI | Microalbuminuria DR |
| Q49 | - |  |  | SI | Fondo de ojo: |
| Q49ObsDR | - |  |  | SI | Fondo de ojo: DR |
| Q50 | - |  |  | SI | ECG Hipertrofia ventricular izquerda: |
| Q51 | - |  |  | SI | Otros Hallazgos: |
| Q52 | - |  |  | SI | VFGe: |
| Q53 | - |  |  | SI | Riesgo Cardio vascular |
| Q54 | - |  |  | SI | VFGE: |
| Q55 | - |  |  | SI | Informada Lab: |
| Q56 | - |  |  | SI | Calculado Mujer: |
| Q57 | - |  |  | SI | Calculado Hombre: |
| Q58 | - |  |  | SI | P. Arterial Diastólica |
| Q58ObsDR | - |  |  | SI | P. Arterial Diastólica DR |
| Q59 | - |  |  | SI | P.Sistolica de Pie |
| Q59ObsDR | - |  |  | SI | P.Sistolica de Pie DR |
| Q60 | - |  |  | SI | IMC (Calcuado) |
| Q61 | - |  |  | SI | Glucosa 60 Min. |
| Q61ObsDR | - |  |  | SI | Glucosa 60 Min. DR |
| Q62 | - |  |  | SI | Glucosa Basal |
| Q62ObsDR | - |  |  | SI | Glucosa Basal DR |
| Q63 | - |  |  | SI | Glucosa 120 Min. |
| Q64 | - |  |  | SI | Calculado Mujer Raza |
| Q65 | - |  |  | SI | Calculado Hombre Raza |
| Q66 | - |  |  | SI | Porcentaje Riesgo Cardiovascular |
| Q66ObsDR | - |  |  | SI | Porcentaje Riesgo Cardiovascular DR |
| Q67 | - |  |  | SI | Riesgo Cardiovascular |
| Q68 | - |  |  | SI | Resultado Riesgo Ulceración Pié Diabético |
| Q68ObsDR | - |  |  | SI | Resultado Riesgo Ulceración Pié Diabético DR |
| Q69 | - |  |  | SI | Resultado Pauta de Enfermedad Renal Crónica |
| Q69ObsDR | - |  |  | SI | Resultado Pauta de Enfermedad Renal Crónica DR |
| Q70 | - |  |  | SI | Edad Paciente |
| Q72 | - |  |  | SI | Estado Nutricional |
| Q72ObsDR | - |  |  | SI | Estado Nutricional DR |
| Q73 | - |  |  | SI | Intolerancia a la Glucosa |
| Q73ObsDR | - |  |  | SI | Intolerancia a la Glucosa DR |
| Q74 | - |  |  | SI | Electrocardiograma |
| Q74ObsDR | - |  |  | SI | Electrocardiograma DR |
| Q75 | - |  |  | SI | TSH |
| Q75ObsDR | - |  |  | SI | TSH DR |
| Q76 | - |  |  | SI | PAP |
| Q76ObsDR | - |  |  | SI | PAP DR |
| Q77 | - |  |  | SI | Sedentarismo |
| Q77ObsDR | - |  |  | SI | Sedentarismo DR |
| Q78 | - |  |  | SI | Colesterol LDL |
| Q78ObsDR | - |  |  | SI | Colesterol LDL DR |
| Q80 | - |  |  | SI | Velocidad de Filtración Glomerular |
| Q80ObsDR | - |  |  | SI | Velocidad de Filtración Glomerular DR |
| Q81 | - |  |  | SI | Riesgo Ulceración Pie Diabético Derecho |
| Q81ObsDR | - |  |  | SI | Riesgo Ulceración Pie Diabético Derecho DR |
| Q82 | - |  |  | SI | Riesgo Ulceración Pie Diabético Izquierdo |
| Q82ObsDR | - |  |  | SI | Riesgo Ulceración Pie Diabético Izquierdo DR |
| Q83 | - |  |  | SI | Etapa Enfermedad Renal Crónica |
| Q83ObsDR | - |  |  | SI | Etapa Enfermedad Renal Crónica DR |
| Q84 | - |  |  | SI | EFAM A |
| Q84ObsDR | - |  |  | SI | EFAM A DR |
| Q85 | - |  |  | SI | EFAM B |
| Q85ObsDR | - |  |  | SI | EFAM B DR |
| Q86 | - |  |  | SI | Fecha Colesterol Total |
| Q87 | - |  |  | SI | Fecha Colesterol HDL |
| Q88 | - |  |  | SI | Fecha Triglicéridos |
| Q89 | - |  |  | SI | Fecha Glicemia |
| Q90 | - |  |  | SI | Fecha HbA1c |
| Q91 | - |  |  | SI | Fecha PTGO |
| Q92 | - |  |  | SI | Fecha Proteinuria |
| Q93 | - |  |  | SI | Fecha Cilindros |
| Q94 | - |  |  | SI | Fecha Hematuria |
| Q95 | - |  |  | SI | Fecha Microalbuminuria |
| Q96 | - |  |  | SI | Fecha Creatinina |
| Q97 | - |  |  | SI | Fecha TSH |
| Q98 | - |  |  | SI | Fecha Fondo de Ojo |
| Q99 | - |  |  | SI | Fecha PAP |
| QAFA | - |  |  | SI | Actividad Física Actual |
| QAFF | - |  |  | SI | Actividad Física Frecuencia |
| QSED | - |  |  | SI | Sedentario |
| QSEDObsDR | - |  |  | SI | Sedentario DR |
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