# TC_hmf_Deploy.InterfaceMessage

**Schema:** TC_hmf_Deploy
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFDEPMSG_ParRef | varchar | PK |  | NO | Interface Parent Reference |
| HMFDEPMSG_Enabled | bit |  |  | SI | Enabled flag |
| HMFDEPMSG_GenClass | varchar |  |  | SI | Message generated class  |
| HMFDEPMSG_MessageDR | bigint |  | FK | SI | DesRef to message code table entry |
| HMFDEPMSG_TransformDR | bigint |  | FK | SI | DesRef to message transformation code table entry |
| HMFDEPMSG_TransformGenClass | varchar |  |  | SI | Message transformation generated class (overrides ... |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*