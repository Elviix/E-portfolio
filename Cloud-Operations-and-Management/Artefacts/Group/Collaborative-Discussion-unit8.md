# Formative Discussion (Unit 8) – Disaster Recovery Plan with Restic
**Activity overview**
**Discussion topic: Design and implementation of a Disaster Recovery (DR) plan for a cloud-based infrastructure, simulating a realistic failure scenario and using an open-source backup tool, with an evaluation of RTO and RPO targets.**
**Duration: Unit 8.**
**Posts included: Initial Post, 1 Peer Response, Tutor Feedback.**

--- 

## Initial Post

I chose a ransomware scenario, simulated by deleting a production directory. The plan was designed for MS Azure, but I could not create a VM: no VM size was available for my subscription, even after changing the region and the size. I therefore implemented it locally on my Kali VM.

I used Restic as the backup and recovery tool. Restic encrypts data client-side and creates snapshots on demand. The repository was stored outside the VM, in a folder shared with the host, so that the backup would survive the loss of the VM.

The Recovery Point Objective (RPO) is the maximum amount of data, measured in time, that can be lost. The Recovery Time Objective (RTO) is the maximum acceptable downtime before the service is restored. For a small business that manages invoices and reports on this server, I set both targets at 60 minutes, one hour of data entry can easily be redone, and a one hour interruption does not block invoicing.

| Event | Time |
|---|---|
| Backup | 08:11:07 |
| Deletion | 08:12:15 |
| Restore started | 08:12:15 |
| Data verified | 08:12:20 |

Figure: Simulated deletion, restoration from snapshot and integrity check
<img width="662" height="222" alt="image" src="https://github.com/user-attachments/assets/3325f5c3-a40f-4a52-8e98-3159365c3b5a" />


The measured RPO was 68 seconds and the RTO 5 seconds. Both targets were met, but these values were coincidental and cannot be generalised: only 39 bytes were restored, locally, with no network transfer and no scheduled backup. I confirmed the integrity of the restored files with cat.

I faced two issues. First, the shared folder (vboxsf) could not delete Restic's lock files, which blocked later operations until I used --no-lock. In a real incident, this would increase the RTO. Second, my first test backed up an old Restic repository instead of the production data, and was still reported as a complete success. This showed me that a backup is only proven when the restored content is checked, which is why I added the cat verification.

To improve this plan, I would schedule hourly backups with cron to guarantee the RPO, store the repository on immutable storage such as Azure Blob with soft delete, and test restoration regularly.

---

## Peer Response 1

I appreciated the honesty with which you reflected on both the successes and limitations of your disaster recovery exercise. I thought the explanation of the ransomware scenario, the use of Restic, and the discussion of RPO and RTO demonstrated a solid understanding of core disaster recovery concepts. What stood out most for me was your acknowledgement that a backup is only truly successful when the restored data is validated. The lesson you learned after initially backing up the wrong repository shows critical thinking and highlights a real-world risk that practitioners often overlook. I also liked that you did not overstate your results and clearly explained that the five-second recovery time and 68-second recovery point were influenced by the small dataset and local environment rather than representing production-scale performance.

How about expanding the validation process beyond using cat to demonstrate file integrity, perhaps through checksums, restoration logs, or Restic verification commands. Also how about a deeper justification of the one-hour RPO and RTO targets from a business impact perspective?

---

## Tutor Feedback

A clear and well-reflected DR test, with accurate explanations of RPO and RTO and a strong recognition that backups must be restored and verified to prove recoverability. Your proposed improvements—scheduled backups, immutable off-site storage, and regular recovery testing—are appropriate. To strengthen the plan, briefly include recovery roles, communication procedures, and a more systematic integrity check.
