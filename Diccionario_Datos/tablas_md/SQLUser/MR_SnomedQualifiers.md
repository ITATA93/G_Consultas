# SQLUser.MR_SnomedQualifiers

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNQ_RowId | bigint | PK |  | NO | - |
| Q04Q1 | - |  |  | SI | Length (cm) |
| Q04Q2 | - |  |  | SI | Note |
| Q04Q3 | - |  |  | SI | Wound Location |
| Q04Q4 | - |  |  | SI | Date |
| Q04Q5 | - |  |  | SI | Actively bleeding |
| Q04Q6 | - |  |  | SI | Numbness or paresthesias distal to wound |
| Q04Q7 | - |  |  | SI | Loss of movement or strength distal to wound |
| Q04Q8 | - |  |  | SI | Foreign body possible |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNQ_Concept_DR | bigint |  | FK | SI | Des Ref Snomed Concept |
| SNQ_Diagnos_DR | varchar |  | FK | SI | Des Ref Diagnos |
| SNQ_Qualifier_DR | bigint |  | FK | SI | Des Ref Qualifier |
| SNQ_Relationship_DR | bigint |  | FK | SI | Des Ref Relationship |
| SNQ_SubjectFindings_DR | varchar |  | FK | SI | Des Ref SubjectFindings |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*