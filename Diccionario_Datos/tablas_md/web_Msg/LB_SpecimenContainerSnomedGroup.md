# web_Msg.LB_SpecimenContainerSnomedGroup

**Schema:** web_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Muestras de Laboratorio**. Gestión de especímenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBSCSG_FullySpecifiedName | varchar |  |  | SI | Fully Specified Name |
| LBSCSG_ParRef | bigint |  |  | SI | - |
| LBSCSG_RowID | varchar |  |  | SI | - |
| LBSCSG_SnomedTermDR | bigint |  | FK | SI | referance to PACSnomedTerms(SNOMED CT)  |
| LBSCSG_SpecimenContainer_DR | bigint |  | FK | SI | Specimen Container |
| LBSCSG_TestSetSnomedGroup_DR | varchar |  | FK | SI | Test Set SNOMED Group |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| TestSetSnomedGroup_DR | varchar |  | FK | SI | Test Set SNOMED Group Message |
| ToBeDelated | bit |  |  | SI | A flag to indicator the recored will be removed wh... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*