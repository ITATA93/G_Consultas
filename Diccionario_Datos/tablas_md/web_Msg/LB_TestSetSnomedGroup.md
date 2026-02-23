# web_Msg.LB_TestSetSnomedGroup

**Schema:** web_Msg
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AddedByTIComment_DR | varchar |  | FK | SI | Not stored in the User class, used to indicate whi... |
| ID | varchar |  |  | NO | - |
| LBTSSG_FullySpecifiedName | varchar |  |  | SI | Fully Specified Name |
| LBTSSG_ParRef | bigint |  |  | SI | - |
| LBTSSG_RowID | varchar |  |  | SI | - |
| LBTSSG_SnomedTermDR | bigint |  | FK | SI | referance to PACSnomedTerms(SNOMED CT)  |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*